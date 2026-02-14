<!--
KFM Governed Artifact
File: data/README.md
-->

# 🧾 `data/` — KFM Governed Data Zones, Registry, Catalogs, Evidence Bundles, & Provenance

![status](https://img.shields.io/badge/status-governed%20artifact-blue)
![evidence](https://img.shields.io/badge/evidence-first-critical)
![policy](https://img.shields.io/badge/policy-OPA%20default%20deny-important)
![zones](https://img.shields.io/badge/zones-Raw%20%E2%86%92%20Work%20%E2%86%92%20Processed-success)
![catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-informational)
![bundles](https://img.shields.io/badge/evidence%20bundle-OCI%20digest%20addressed-informational)
![hashing](https://img.shields.io/badge/hashing-spec__hash%20%2B%20sha256-important)
![attest](https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20SLSA%20attestations-informational)
![registry](https://img.shields.io/badge/build%20driver-dataset%20registry-success)

> [!IMPORTANT]
> `data/` is a **governed system boundary**. Any change here can affect:
> - what the API is allowed to serve
> - what the UI can cite (and resolve)
> - what Story Nodes may publish
> - what Focus Mode may answer (cite‑or‑abstain)
> - what auditors can verify
>
> **Rule of thumb:** if you can’t point to **processed artifacts + checksums + catalogs + lineage**, it is **not** servable.

---

## Alignment snapshot

This README is aligned to KFM-NG’s documented invariants:
- promotion gates and catalogs must exist **before** scaling to many datasets
- dataset integrations are **registry-driven deliverables**, not ad-hoc drops
- every served result must carry **evidence bundle + citations + audit reference**

> [!NOTE]
> If this README and the implementation ever diverge, treat it as a **governance incident** and resolve via ADR + CI gates.

---

## Table of contents

- [Non‑negotiables](#nonnegotiables)
- [Quick workflow: add or update a dataset](#quick-workflow-add-or-update-a-dataset)
- [Directory layout](#directory-layout)
- [Truth path: how data becomes servable](#truth-path-how-data-becomes-servable)
- [Registry: the build driver](#registry-the-build-driver)
- [Data zones](#data-zones)
- [Promotion contract: what “publishable” means](#promotion-contract-what-publishable-means)
- [Deterministic hashing: `spec_hash` + checksums](#deterministic-hashing-spec_hash--checksums)
- [Catalogs: DCAT, STAC, PROV](#catalogs-dcat-stac-prov)
- [Evidence bundles & canonical addressing](#evidence-bundles--canonical-addressing)
- [Audit & evidence resolution](#audit--evidence-resolution)
- [Sensitivity, CARE/FAIR taxonomy, and redaction](#sensitivity-carefair-taxonomy-and-redaction)
- [Connectors, watchers, and backfills](#connectors-watchers-and-backfills)
- [Formats & normalization standards](#formats--normalization-standards)
- [CI gates & Definition of Done](#ci-gates--definition-of-done)
- [Operations & monitoring](#operations--monitoring)
- [Appendix: Templates](#appendix-templates)
- [Governance review triggers](#governance-review-triggers)
- [Glossary](#glossary)

---

## Non‑negotiables

These are **system invariants**. Breaking them breaks KFM governance.

1) **Trust membrane**
   - UI and external clients never access databases or object storage directly.
   - All access is through the **governed API + policy boundary + audit logging**.

2) **Fail‑closed policy**
   - Authorization is **default deny**.
   - If evidence is missing or ambiguous, deny/abstain rather than “best guess.”

3) **Registry-driven integrations**
   - Every dataset must be registered before ingestion/promotion.
   - The registry is the authoritative inventory and build plan (prevents “forgotten sources”).

4) **Mandatory promotion gates**
   - Data flows **Raw → Work → Processed**.
   - Promotion is blocked unless checksums + validation + catalogs + lineage exist.

5) **Processed is the only publishable source of truth**
   - Raw/work are never served (directly or indirectly).

6) **Cite‑or‑abstain everywhere**
   - API answers and Focus Mode responses must include citations **or abstain**.
   - Every response must include an `audit_ref` and an evidence bundle reference.

---

## Quick workflow: add or update a dataset

> [!TIP]
> Keep this fast and repeatable. A dataset integration should feel like “run the playbook,” not “invent a new pipeline.”

1) **Register the dataset**
   - Add or update a dataset integration profile in `data/registry/…`
   - Define: license, cadence, sensitivity expectations, connector config, and backfill policy.

2) **Add or update the raw manifest**
   - Add `data/raw/<dataset_id>/manifest.yml`
   - Raw is append-only: new versions = new manifests or new manifest revisions with their own hashes.

3) **Run ingest (containerized)**
   - Pipeline writes work artifacts:
     - run record/receipt
     - validation report
     - QA report(s)
     - provisional lineage (PROV activity)

4) **Promote**
   - Pipeline writes processed artifacts + checksums
   - Generate/validate catalogs (DCAT always; STAC/PROV as applicable)
   - Produce an **evidence bundle reference** (digest-first)

5) **CI enforces promotion**
   - Catalog validation, hash verification, policy tests, contract tests
   - Optionally: verify SBOM/SLSA attestations for the evidence bundle

6) **Indexes refresh from catalogs**
   - PostGIS/Graph/Search rebuilds are derived from canonical catalogs & processed artifacts
   - No “hand edits” in downstream stores

---

## Directory layout

> [!IMPORTANT]
> The layout below is the **KFM-NG target layout** for a governed repo. If your repo differs, either:
> - migrate toward this, or
> - document the deviation in an ADR + update the validators accordingly.

```text
data/
├─ README.md
│
├─ registry/                               # authoritative dataset inventory + integration profiles
│  ├─ datasets/                            # one profile per dataset_id (YAML/JSON)
│  │  └─ <dataset_id>.yml
│  ├─ policy_taxonomy.yml                  # controlled vocabulary (sensitivity/CARE/FAIR/redistribution)
│  └─ schemas.lock.yml                     # pinned schema/tool versions used by validators (optional)
│
├─ raw/                                    # immutable inputs or fetch manifests (never served)
│  └─ <dataset_id>/
│     ├─ manifest.yml                      # governed raw manifest (license + sensitivity required)
│     ├─ checksums.txt                     # sha256 for raw assets (or pointers) referenced by manifest
│     └─ pointers/                         # optional: pointer files (object store / upstream URLs)
│
├─ work/                                   # regeneratable intermediates; QA and profiling (never served)
│  └─ <dataset_id>/
│     └─ runs/<run_id>/                    # run-scoped artifacts (do not overwrite prior runs)
│        ├─ run_record.json                # aka run_receipt: inputs/outputs/spec_hash/tooling
│        ├─ validation_report.json         # schema/license/sensitivity/geo/time checks
│        ├─ qa/report.json                 # quick QC summary (machine-readable)
│        ├─ profiling/                     # drift stats, samples, geometry error logs
│        └─ scratch/                       # temp outputs (gitignored recommended)
│
├─ processed/                              # publishable artifacts (servable); immutable per version_id
│  └─ <dataset_id>/
│     └─ <version_id>/
│        ├─ data.parquet                   # or GeoParquet / partitioned layout
│        ├─ tiles/                         # optional: prebuilt tiles
│        ├─ media/                         # optional: publishable derivatives (PDF/PNG/etc)
│        ├─ checksums.txt                  # sha256 for every published artifact in this version
│        └─ evidence_bundle.ref.json       # canonical bundle digest + resolver href (digest-first)
│
└─ catalog/                                # machine-readable catalogs consumed by runtime services
   ├─ dcat/
   │  ├─ <dataset_id>.json                 # dataset-level DCAT (may list versions/distributions)
   │  └─ <dataset_id>/<version_id>.json    # version/distribution record (recommended for immutability)
   ├─ stac/
   │  └─ <dataset_id>/
   │     ├─ collection.json                # one collection per dataset/product
   │     └─ items/<version_id>/*.json      # items grouped by version_id (or time slices)
   └─ prov/
      └─ <dataset_id>/
         └─ run_<run_id>.json              # PROV activity + entities linking raw→work→processed
```

---

## Truth path: how data becomes servable

```mermaid
flowchart LR
  REG[Registry\n(dataset profiles)] --> RAW[Raw zone\n(manifest + checksums)]
  RAW --> WORK[Work zone\n(run record + validation + QA)]
  WORK --> PROC[Processed zone\n(immutable versioned artifacts)]
  PROC --> CATS[Catalogs\nDCAT + STAC + PROV]
  CATS --> BUNDLE[Evidence bundle\n(OCI digest addressed)]
  BUNDLE --> STORES[Stores\n(PostGIS / Graph / Search / Object Store)]
  STORES --> API[GOVERNED API\n(auth + policy + redaction + audit)]
  API --> UI[Web UI\n(map/time/story)]
  UI --> STORIES[Story Nodes\n(governed narratives)]
  STORIES --> FOCUS[Focus Mode\n(cite-or-abstain)]
```

> [!IMPORTANT]
> **Only `processed/` + `catalog/` are eligible to be served** (directly or indirectly).
> Raw/work exist to support reproducibility, QA, and auditability.

---

## Registry: the build driver

The **registry** is the authoritative system for:
- what datasets exist
- how they are ingested (connector configuration)
- how they are validated (required gates)
- how they are classified (license/sensitivity/policy tags)
- how backfills are performed (explicit, versioned)

### What belongs in a dataset profile (minimum)
- `dataset_id` + upstream identifiers
- access mechanism + cadence
- license + attribution requirements
- sensitivity defaults + redaction policy
- validation requirements + thresholds
- storage targets (tabular/geo/raster/artifact)
- backfill policy (ranges, batching, expected runtime)
- provider compliance constraints (rate limits, ToS, row limits, consent requirements)

> [!NOTE]
> The README is not the inventory. The registry is.

---

## Data zones

| Zone | Servable? | Mutability | What belongs here | What must *never* happen |
|---|---:|---|---|---|
| `raw/` | ❌ | Append-only / immutable per asset | Source drops, fetch manifests, upstream identifiers, raw checksums | Editing raw history; serving raw to users |
| `work/` | ❌ | Regeneratable | Run-scoped work products: run record, validation, QA, profiling | Treating work as truth; publishing directly |
| `processed/` | ✅ | Immutable per `version_id` | Final publishable artifacts + checksums + bundle ref | Mutating an already published version |
| `catalog/` | ✅ (metadata) | Append-only by version | DCAT/STAC/PROV records; cross-links; schema-validated JSON | Missing/broken cross-links; catalogs that don’t match hashes |

---

## Promotion contract: what “publishable” means

Promotion is a **contract**, not a convenience.

### Required promotion evidence (minimum)
A dataset version is publishable only if **all** of these exist and validate:

- **Raw**: manifest + raw checksums
- **Work**: run record + validation report + QA report
- **Processed**: artifacts + checksums
- **Catalogs**:
  - DCAT (always)
  - STAC (if spatial assets)
  - PROV (lineage chain)
- **Evidence bundle reference** (digest-first, canonical addressing)
- **Policy labels** attached and enforceable (public/restricted/sensitive-location/etc.)
- **API contract tests** for at least one representative query
- **Audit event** recorded on promotion and on serve

### Promotion gate checklist (CI-enforced)
- [ ] Raw assets checksummed and addressable by content hash
- [ ] License present and propagated into catalogs
- [ ] Sensitivity + policy tags present and propagated into policy labels
- [ ] Schema validation passes (required fields, types, null thresholds)
- [ ] Geospatial validation passes (valid geometries, CRS declared, bounds sane)
- [ ] Temporal validation passes (ranges sane, time model requirements met)
- [ ] QA report stored as a run artifact with a stable ID
- [ ] Processed artifacts are immutable, with `checksums.txt` computed
- [ ] Catalog writers succeed (DCAT/STAC/PROV well-formed + link-check clean)
- [ ] Evidence bundle reference created (digest-first)
- [ ] (If enabled) SBOM + SLSA attestations verified for bundle digest
- [ ] API contract tests pass
- [ ] Audit record appended, referencing `run_id` + `version_id`

---

## Deterministic hashing: `spec_hash` + checksums

Two different hash families exist and both are required:

### 1) `checksums.txt` (content integrity)
- Purpose: prove that **bytes** served match the bytes that were promoted
- Scope: every raw and processed artifact

Format: `sha256 <hex>  <relative_path>` (sha256sum style)

### 2) `spec_hash` (semantic spec identity)
- Purpose: prove that **the same spec** leads to the same identifiers / ETags / receipts
- Scope: manifests, run records/receipts, connector specs, catalog writer inputs

**Standard definition (KFM):**
- `spec_hash = sha256(JCS(spec))`
- where `spec` is a schema-defined object
- and JCS means RFC 8785 JSON Canonicalization Scheme
- store alongside:
  - `spec_schema_id`
  - `spec_recipe_version` (semver)

> [!WARNING]
> If different teams compute “spec_hash” differently, hashes become incomparable and audits can’t establish equivalence.

---

## Catalogs: DCAT, STAC, PROV

KFM uses catalogs to make data:
- discoverable (DCAT)
- mappable + time-addressable (STAC)
- reproducible + auditable (PROV)

### DCAT (dataset discovery)
DCAT entries must capture:
- dataset identity and description
- publisher/maintainer contact (where applicable)
- license + attribution text
- distributions pointing to processed artifacts (or bundle resolver)
- update frequency / cadence

### STAC (spatiotemporal assets)
STAC is required for spatial assets (vectors/rasters/footprints):
- spatial extent (bbox)
- temporal extent (interval)
- asset media types + roles
- link to DCAT dataset and PROV lineage (KFM profile)

> [!NOTE]
> KFM must pin and enforce a single STAC baseline + extension policy (via validator).

### PROV (lineage)
PROV is the lineage spine:
- raw inputs → work steps → processed outputs
- links every derived artifact to inputs + activity + agent/tooling
- includes deterministic hashes for promoted artifacts

---

## Evidence bundles & canonical addressing

KFM treats “where is the data?” as a governed question.

### Canonical addressing hierarchy (must be consistent)
1) **Evidence bundle digest address** (canonical)
2) **Stable gateway URL derived from digest** (servable)
3) **Storage URLs** (implementation detail; never relied on by UI citations)

### Evidence bundle contents (recommended minimum)
- catalogs (DCAT/STAC/PROV)
- processed artifacts (or pointers)
- run record/receipt + validation + QA
- SBOM + SLSA provenance attestations (if enabled)
- signatures / transparency proofs (if enabled)

> [!IMPORTANT]
> The bundle digest is the **canonical reference** used by citations and audit resolution.

---

## Audit & evidence resolution

KFM treats provenance and audit as **queryable first-class objects**.

### Evidence resolution requirement
All citations/provenance references must be resolvable by the governed API.

Canonical “citation kinds”:
- `dcat`
- `stac`
- `prov`
- `doc`
- `graph`

### Citation object (minimum)
```yaml
Citation:
  required: [id, kind, ref]
  properties:
    id: string
    kind: dcat|stac|prov|doc|graph
    ref: string
    locator: string   # page/span/time/bbox/feature_id/etc.
    note: string
```

### Audit record expectations (minimum)
- `audit_ref`
- timestamps
- actor metadata (role/claims)
- event type + subject/resource
- evidence bundle digest + citations
- integrity chaining (`prev_hash`, `event_hash`) for tamper evidence

---

## Sensitivity, CARE/FAIR taxonomy, and redaction

KFM handles sensitive data explicitly and conservatively.

### Controlled vocabulary (must exist)
Define a small, enforced taxonomy covering:
- classification levels (public / restricted / …)
- culturally/tribally sensitive flags
- redistribution rules / license constraints
- sensitive-location precision rules
- PII risk flags

> [!IMPORTANT]
> These tags are **enforceable inputs** to policy, not documentation.

### Sensitive locations: split assets (recommended)
- Public/generalized geometry: servable
- Restricted/precise geometry: separate artifact/store
- Access authorized by policy on read
- UI must not fetch precise geometry without explicit grant
- All generalization/suppression is recorded in PROV

---

## Connectors, watchers, and backfills

### Connector phases (conceptual)
1) discover capabilities  
2) acquire raw data (manifested + checksummed)  
3) normalize + enrich (work artifacts)  
4) validate (reports)  
5) publish (processed + catalogs + bundle ref)  

### Watchers (for frequently changing sources)
- must respect provider compliance constraints
- use conditional requests (ETag / Last-Modified)
- structured backoff + retry policies
- emit delta receipts (what changed, when, why)

### Backfills
- always explicit runs with their own provenance
- never overwrite prior releases
- backfill scope and batching defined in registry

---

## Formats & normalization standards

### Canonical normalization (minimum)
- Text encoding: UTF‑8
- Geometry CRS: WGS84 (declare explicitly)
- Time: ISO 8601 (UTC where applicable)

### Recommended publish formats
- Tabular: Parquet (processed)
- Vectors: GeoParquet (processed); GeoJSON (work, for debugging)
- Rasters: Cloud-Optimized GeoTIFF (COG) (processed)
- Artifacts/media: PDF/JPEG/PNG (originals + derivatives with provenance)

---

## CI gates & Definition of Done

### CI minimal hardening set (data-related)
- Validate raw manifest schema + `spec_hash`
- Validate run record + validation/QA reports
- Validate processed checksums
- Validate DCAT/STAC/PROV outputs + cross-links
- Run OPA policy unit/regression tests (default deny; cite‑or‑abstain)
- Run API contract tests for:
  - catalogs/layers
  - evidence resolution
  - at least one representative dataset query
- (If enabled) Verify SBOM + SLSA attestations for evidence bundle digest

### Definition of Done (dataset integration ticket)
- [ ] Dataset profile exists in registry
- [ ] Raw manifest + raw checksums produced deterministically
- [ ] Normalization emits canonical schema and/or STAC assets
- [ ] Validation gates implemented and enforced in CI
- [ ] Policy labels defined; restricted fields/locations redacted per rules
- [ ] Catalogs emitted and link-check clean
- [ ] Evidence bundle reference present (digest-first)
- [ ] API contract tests pass (one representative query minimum)
- [ ] Backfill strategy documented (ranges + expected runtime)

---

## Operations & monitoring

### Freshness SLOs (per dataset)
Each dataset declares a freshness expectation based on cadence:
- sub-hourly (real-time sensors)
- daily/weekly (periodic sources)
- exempt (static archives)

### Observability signals (minimum)
- ingest runs: success/fail, duration, rows/bytes, retries
- freshness: last successful run timestamp vs expected cadence
- drift: missingness, distribution shifts, geometry error rate
- API: latency, cache hits, policy denials, evidence resolution failures
- index drift: rebuild from canonical catalogs + diff checks

---

## Appendix: Templates

<details>
<summary><strong>Template: <code>data/raw/&lt;dataset_id&gt;/manifest.yml</code> (illustrative)</strong></summary>

```yaml
dataset_id: example_dataset
title: "Example Dataset"
source:
  type: http
  uri: "https://example.org/source.csv"
license: "CC-BY-4.0"
attribution: "Example Publisher"
sensitivity:
  level: public        # must be in controlled vocabulary
  tags: [fair:open]    # must be in controlled vocabulary
expected_files:
  - name: source.csv
    sha256: "..."
```
</details>

<details>
<summary><strong>Template: <code>run_record.json</code> (aka run receipt)</strong></summary>

```json
{
  "run_id": "run_2026_02_14T120000Z_abc123",
  "dataset_id": "example_dataset",
  "spec_schema_id": "kfm.schema.run_record.v1",
  "spec_recipe_version": "1.0.0",
  "spec_hash": "sha256:...",
  "inputs": [{ "uri": "data/raw/example_dataset/source.csv", "sha256": "..." }],
  "code": { "git_sha": "...", "image": "kfm/pipeline:..." },
  "outputs": [{ "uri": "data/processed/example_dataset/<version_id>/data.parquet", "sha256": "..." }],
  "validation_report": "data/work/example_dataset/runs/<run_id>/validation_report.json",
  "prov_ref": "data/catalog/prov/example_dataset/run_<run_id>.json"
}
```
</details>

<details>
<summary><strong>Template: <code>processed/.../evidence_bundle.ref.json</code></strong></summary>

```json
{
  "bundle_digest": "sha256:...",
  "canonical_resolver": "/bundles/sha256:...",
  "includes": ["dcat", "stac", "prov", "run_record", "validation", "checksums"]
}
```
</details>

---

## Governance review triggers

Route for governance review if any of the following are true:
- precise archaeological/historic site locations
- culturally restricted knowledge
- personal data / ownership names / PII risk
- small-area health or public safety counts enabling re-identification
- datasets with redistribution constraints beyond the standard licenses

---

## Glossary

- **Dataset**: governed unit of data with license + sensitivity + versioning.
- **DatasetVersion**: immutable published version (content-hashable).
- **Registry**: authoritative dataset inventory + integration configuration.
- **Raw / Work / Processed**: promotion zones enforcing provenance and publishability.
- **Catalogs**: DCAT/STAC/PROV metadata consumed by runtime services.
- **Evidence bundle**: digest-addressed package of artifacts + metadata + receipts for audit/citations.
- **Audit ledger**: append-only record of access, decisions, and evidence references.
