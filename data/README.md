# 🧾 `data/` — KFM Governed Data Zones, Catalogs, & Provenance

![status](https://img.shields.io/badge/status-governed%20artifact-blue)
![evidence](https://img.shields.io/badge/evidence-first-critical)
![policy](https://img.shields.io/badge/policy-OPA%20default%20deny-important)
![catalogs](https://img.shields.io/badge/catalogs-STAC%20%7C%20DCAT%20%7C%20PROV-informational)
![zones](https://img.shields.io/badge/data%20zones-Raw%20%E2%86%92%20Work%20%E2%86%92%20Processed-success)

> [!IMPORTANT]
> This directory is a **governed system boundary**: it implements the *truth path* for KFM data.
> If you change anything under `data/`, assume it can affect:
> - what the API is allowed to serve
> - what the UI can cite
> - what Focus Mode can answer
> - what auditors can verify

---

## Table of contents

- [Non‑negotiables](#nonnegotiables)
- [Directory layout](#directory-layout)
- [Truth path (how KFM data becomes “servable”)](#truth-path-how-kfm-data-becomes-servable)
- [Data zones](#data-zones)
- [Catalogs: DCAT, STAC, PROV](#catalogs-dcat-stac-prov)
- [Promotion gate checklist (CI‑enforced)](#promotion-gate-checklist-ci-enforced)
- [Pipeline artifacts](#pipeline-artifacts)
- [Audit ledger & evidence resolution](#audit-ledger--evidence-resolution)
- [Sensitivity, FAIR/CARE, and redaction](#sensitivity-faircare-and-redaction)
- [Connector contract & orchestration](#connector-contract--orchestration)
- [Canonical IDs, joins, and alignment](#canonical-ids-joins-and-alignment)
- [Formats & normalization standards](#formats--normalization-standards)
- [Data source register](#data-source-register)
- [CI gates, tests, and Definition of Done](#ci-gates-tests-and-definition-of-done)
- [Operations & monitoring](#operations--monitoring)
- [Appendix: Templates](#appendix-templates)

---

## Non‑negotiables

These rules are **system invariants**. Breaking them breaks KFM governance.

1) **Trust membrane**  
   UI and external clients **never** access databases directly. All access is through the **governed API + policy boundary**.

2) **Fail‑closed policy on every request**  
   If the system is uncertain, policy must deny (default‑deny posture).

3) **Dataset promotion gates are mandatory**  
   Data must move **Raw → Work → Processed**. Promotion requires **checksums + catalogs** (STAC/DCAT/PROV).

4) **Processed zone is the only publishable source of truth**  
   Raw/Work are **never** served to users.

5) **Focus Mode must cite or abstain**  
   Every answer must either include citations or abstain; every response must carry an **audit reference**.

> [!NOTE]
> This README documents the *data side* of those guarantees: zones, catalogs, validation gates, and operational expectations.

---

## Directory layout

> [!TIP]
> Keep this directory **reviewable**. Prefer *manifests + catalogs + checksums* over committing huge binary drops.
> Large assets should be tracked via object storage pointers and strong hashes (recommended, not confirmed in repo).

```text
data/
├─ README.md                      # ← you are here
│
├─ raw/                           # immutable source drops OR fetch manifests (never served)
│  └─ <dataset_id>/
│     ├─ manifest.json            # governed raw manifest (license + sensitivity required)
│     └─ ...                      # source drops (only if feasible), or pointer files
│
├─ work/                          # intermediate artifacts; regeneratable; QA + profiling (never served)
│  └─ <dataset_id>/
│     ├─ run_record.json
│     ├─ validation_report.json
│     ├─ profiling/               # stats, drift reports, geometry error samples
│     └─ scratch/                 # temp outputs (gitignored recommended)
│
├─ processed/                     # publishable artifacts with required checksums + catalogs (servable)
│  └─ <dataset_id>/
│     └─ <version_id>/            # immutable once published
│        ├─ data.parquet          # or GeoParquet, or partitioned layout
│        ├─ tiles/                # prebuilt tiles (optional)
│        ├─ media/                # derived publishable media (optional)
│        └─ checksums.sha256      # sha256 for every published artifact
│
└─ catalog/                       # machine-readable catalogs consumed by runtime services
   ├─ dcat/
   │  └─ <dataset_id>/<version_id>.json
   ├─ stac/
   │  └─ <dataset_id>/collection.json
   │     └─ items/<version_id>/*.json
   └─ prov/
      └─ <dataset_id>/run_<run_id>.json
```

---

## Truth path (how KFM data becomes “servable”)

KFM’s **truth path** is:

```mermaid
flowchart LR
  RAW[Raw zone\n(immutable inputs)] --> WORK[Work zone\n(intermediates + QA)]
  WORK --> PROC[Processed zone\n(publishable artifacts)]
  PROC --> CATS[Catalogs\nDCAT + STAC + PROV]
  CATS --> STORES[Stores\n(PostGIS / Graph / Search / Object Store)]
  STORES --> API[GOVERNED API\n(policy + redaction + audit)]
  API --> UI[Web UI\n(map/time/story)]
  UI --> STORIES[Story Nodes\n(governed narratives)]
  STORIES --> FOCUS[Focus Mode\n(cite-or-abstain)]
```

> [!IMPORTANT]
> **Only `processed/` + `catalog/` are eligible to be served** (directly or indirectly).  
> Everything else exists to support reproducibility and auditability.

---

## Data zones

| Zone | Servable? | Mutability | What belongs here | What must *never* happen |
|---|---:|---|---|---|
| `raw/` | ❌ | Immutable | Source drops or fetch manifests; upstream identifiers; license & sensitivity declarations | Editing raw history; serving raw to UI/API consumers |
| `work/` | ❌ | Regeneratable | Intermediate transforms; validation reports; profiling; QA artifacts | Treating work as “truth”; publishing directly |
| `processed/` | ✅ | Immutable per version | Final publishable artifacts; partitioned data; tile cache; publishable derivatives | Mutating an already published version |
| `catalog/` | ✅ (metadata) | Append-only by version | DCAT, STAC, PROV records; cross-links; schema-validated JSON | Missing/broken cross-links; catalogs that don’t match hashes |

---

## Catalogs: DCAT, STAC, PROV

KFM uses standard, machine-readable catalogs to make data:

- discoverable (DCAT)
- mappable & time-addressable (STAC)
- reproducible & auditable (PROV)

### DCAT (dataset discovery)
DCAT entries should capture at minimum:
- dataset identity
- license + attribution
- distributions (downloadURL / accessURL) pointing to processed artifacts
- version linkage (recommended)

### STAC (spatiotemporal assets)
STAC is required when a dataset is a spatial asset (vectors/rasters/footprints).
Minimum expectations for a KFM STAC collection:
- license
- spatial extent (bbox)
- temporal extent (interval)
- link to DCAT entry (recommended KFM profile)

### PROV (lineage)
PROV is the *lineage spine*. It should link:
- raw inputs → work steps → processed outputs
- with deterministic hashes of published artifacts
- and a stable `run_id`/activity identifier

> [!NOTE]
> Validators should enforce a “KFM profile” for each standard (recommended):  
> STAC↔DCAT↔PROV must cross-link and must be resolvable by the evidence resolver.

---

## Promotion gate checklist (CI‑enforced)

Promotion to `processed/` **must be blocked** unless all of the following are true:

- [ ] License present (and carried into DCAT)
- [ ] Sensitivity classification present (and carried into policy labels)
- [ ] Schema checks pass (types/required fields/null thresholds)
- [ ] Geospatial checks pass (geometry validity/bounds/CRS declared where applicable)
- [ ] Checksums computed for *every* processed artifact
- [ ] STAC/DCAT/PROV artifacts exist, validate, and cross-link correctly
- [ ] Audit event recorded (audit ledger append)
- [ ] Human approval recorded if sensitive/high-risk (as required by governance)

---

## Pipeline artifacts

Every dataset integration produces a consistent set of “governed artifacts”.

### Required artifacts (minimum)
- **Raw manifest** (`data/raw/<dataset_id>/manifest.json`)
- **Run record** (`data/work/<dataset_id>/run_record.json`)
- **Validation report** (`data/work/<dataset_id>/validation_report.json`)
- **Checksums** (`data/processed/<dataset_id>/<version_id>/checksums.sha256`)
- **Catalogs**:
  - DCAT: `data/catalog/dcat/<dataset_id>/<version_id>.json`
  - STAC (if spatial): `data/catalog/stac/<dataset_id>/collection.json` + items
  - PROV: `data/catalog/prov/<dataset_id>/run_<run_id>.json`

> [!IMPORTANT]
> “I ran it locally” is not evidence.  
> **Run records + validation reports + catalogs + hashes** are the evidence.

---

## Audit ledger & evidence resolution

KFM treats provenance and audit as **queryable first-class objects**.

### Evidence resolver requirement
All citations/provenance references must be resolvable via an API endpoint using stable URI schemes such as:
- `prov://...`
- `stac://...`
- `dcat://...`
- `doc://...`
- `graph://...`

**Acceptance criterion (recommended):** given a `citation.ref`, the UI can resolve it to a human-readable evidence view in ≤ 2 API calls.

### Audit record expectations
Audit records should include:
- an `audit_ref`
- timestamps
- actor metadata (role, attributes)
- event type + subject
- evidence references
- integrity chaining (`prev_hash`, `event_hash`) for tamper evidence

> [!NOTE]
> Implementation hint (documented pattern): append-only audit ledger table + periodic checkpointing to object storage with checksums (tamper-evident), tied to PROV‑O identifiers.

---

## Sensitivity, FAIR/CARE, and redaction

KFM must handle sensitive data explicitly and conservatively.

### Recommended sensitivity classes
- **Public**: safe to publish without redaction.
- **Restricted**: requires role-based access (example: ownership names).
- **Sensitive-location**: coordinates must be generalized/suppressed (archaeology, sensitive species).
- **Aggregate-only**: publish only above thresholds to prevent re-identification (health/crime small counts).

### Redaction is a first-class transformation
Redaction must be recorded in PROV:
- Raw remains immutable.
- Redacted derivative is a separate DatasetVersion (often a separate `dataset_id`).
- Policy labels must be documented.

> [!WARNING]
> Never “silently” mask or merge.  
> If you generalize, suppress, or aggregate—**record it** (PROV) and enforce it (policy).

---

## Connector contract & orchestration

Connectors standardize how sources enter KFM.

### Connector interface (conceptual)
Connectors should support these phases:
1) discover capabilities  
2) acquire raw data (manifested)  
3) transform to work artifacts  
4) validate (produce a report)  
5) publish (produce a DatasetVersionRef)

### Scheduling & backfills
- Schedule connectors by cadence (real-time, daily, weekly, annual, static).
- Jobs must be **idempotent**: re-running a job must not mutate an already published DatasetVersion.
- Backfills are explicit runs with their own audit trail.

### Operational metadata (minimum)
Each run should capture:
- start/end timestamps
- rows read/written
- error counts
- latency
- freshness signals

> [!IMPORTANT]
> Secrets must never be committed. Store auth material in a vault/secret store (recommended).

---

## Canonical IDs, joins, and alignment

KFM’s goal is cross-source reasoning without losing provenance.

### Dataset identity & versions
- Persist `dataset_id` + upstream identifiers.
- Treat `version_id` as a deterministic **content-hash of the raw manifest** (recommended pattern).
- Preserve stable per-record `source_record_id` for citations.

### Cross-source alignment (joins that make stories possible)
- **Geography**: normalize to GeoIDs; maintain boundary vintages + crosswalks.
- **Time**: normalize to a shared time model; store both reported and derived timestamps.
- **Entity resolution**: match cautiously; record confidence; never merge silently.
- **Events**: create event nodes and link supporting observations/artifacts as evidence.

---

## Formats & normalization standards

### Canonical normalization (minimum)
- Text encoding: **UTF‑8**
- Geometry CRS: **WGS84**
- Time: **ISO 8601**

### Recommended publish formats
- Tabular: JSON/CSV (raw), Parquet (processed)
- Vectors: GeoJSON (work), (Geo)Parquet (processed)
- Rasters: Cloud-Optimized GeoTIFF (COG) (processed)
- Artifacts/media: PDF/JPEG/PNG (originals + derivatives with provenance)

### Satellite ingestion pattern (STAC-first)
When integrating earth-observation imagery:
- one STAC Collection per product
- items per scene/tile/time with footprints
- store metadata + pointers when too large to mirror
- preserve original references in PROV; standardize derivatives

---

## Data source register

A data source register turns the “inventory” into buildable integration profiles.

### What belongs in the register
Each source entry should include:
- domain
- access mechanism
- cadence
- license
- sensitivity expectations
- connector configuration defaults
- canonical mapping notes

### Example entries (illustrative subset)
| Domain | Data source | Access | Cadence | License | Sensitivity |
|---|---|---|---|---|---|
| Biodiversity | GBIF | API + bulk (DwC-A/CSV) | Continuous | Open (varies) | Low |
| Biodiversity | iNaturalist | API + exports | Continuous | Varies | Medium (precise locations) |
| Climate | NOAA NCEI (CDO) | API + bulk | Daily/monthly | Public domain | Low |
| Climate | Kansas Mesonet | CSV + API | 5–60 min | Open access | Low |
| Wildlife | eBird | API + products | Frequent | Terms apply | Medium (sensitive species) |

> [!NOTE]
> The full register should live as a governed machine-readable file (recommended; not confirmed in repo),
> and each source should be expanded into an implementation profile.

---

## CI gates, tests, and Definition of Done

### CI minimal hardening set (data-related)
- Validate catalogs (STAC/DCAT/PROV) for any new/changed dataset
- Run OPA policy tests (default deny + cite-or-abstain)
- Validate governed schemas and reports

### Data validator rule set (recommended minimum)
Validators should produce deterministic, machine-readable JSON reports covering:
- schema validation
- geospatial validation
- temporal validation
- license validation
- sensitivity validation
- catalog validation (STAC/DCAT/PROV + cross-links)
- hash validation (sha256 for every processed artifact referenced in catalogs)

### Policy regression suite (must-not-regress)
- “Golden queries” that once leaked restricted fields must fail forever
- Negative tests for sensitive-location precision controls
- Field-level tests for redaction (owner names, small counts, exact site coordinates)
- Audit integrity tests: every API response includes audit reference + evidence bundle hash

### Integration ticket Definition of Done (dataset/source)
- [ ] Connector implemented and registered in the data-source registry config
- [ ] Raw acquisition produces deterministic manifest + checksums
- [ ] Normalization emits canonical schema and/or STAC assets
- [ ] Validation gates implemented and enforced in CI
- [ ] Policy labels defined; restricted fields/locations redacted per rules
- [ ] Catalogs emitted (DCAT always; STAC/PROV as applicable) and link-check clean
- [ ] API contract tests pass for at least one representative query
- [ ] Backfill strategy documented (historic ranges + expected runtime)

---

## Operations & monitoring

Operational discipline prevents datasets from silently going stale.

### Freshness SLOs (per dataset)
Each dataset should carry a freshness expectation based on its cadence
(e.g., sub-hourly for real-time sensors; days/weeks for periodic sources; exempt for static archives).

### Observability signals (minimum)
- ingest runs: success/fail, duration, rows/bytes, retries
- freshness: last successful run timestamp + expected cadence
- quality drift: distribution checks, missingness, geometry errors
- API: latency, cache hits, policy denials, evidence resolution failures
- storage: object growth, PostGIS index health, search index lag

---

## Appendix: Templates

<details>
<summary><strong>Template: <code>run_record.json</code> (illustrative)</strong></summary>

```json
{
  "run_id": "run_...",
  "dataset_id": "example_dataset",
  "inputs": [{"uri":"data/raw/example.csv","sha256":"..."}],
  "code": {"git_sha":"...","image":"kfm/pipeline:..."},
  "outputs": [{"uri":"data/processed/example.parquet","sha256":"..."}],
  "validation_report": "data/work/example/validation_report.json",
  "prov_ref": "data/catalog/prov/example/run_....json"
}
```
</details>

<details>
<summary><strong>Template: Promotion “abstain” response pattern (Focus Mode)</strong></summary>

```json
{
  "answer_markdown": "I can't answer that from the verified KFM sources available for this view. Try narrowing the time range or selecting relevant layers.",
  "citations": [],
  "audit_ref": "audit_..."
}
```
</details>

<details>
<summary><strong>Template: Citation object (kinds + refs)</strong></summary>

```yaml
Citation:
  required: [id, kind, ref]
  properties:
    id: string
    kind: dcat|stac|prov|doc|graph
    ref: string
    locator: string   # page/span/time/bbox/etc.
    note: string
```
</details>

---

## Governance review triggers (quick list)

Route for governance review if any of the following are true:
- precise archaeological/historic site locations
- culturally restricted knowledge
- personal data / ownership names
- small-area health or public safety counts that could enable re-identification
- any dataset requiring “restricted” or “sensitive-location” handling

---

## Glossary (data-facing)

- **Dataset**: governed unit of data with license + sensitivity + versioning.
- **DatasetVersion**: immutable published version (content-hashable).
- **Raw / Work / Processed**: promotion zones enforcing provenance and publishability.
- **Catalogs**: machine-readable metadata (DCAT/STAC/PROV) consumed by runtime services.
- **Evidence**: resolvable references that support claims, layers, and answers.
- **Audit ledger**: append-only record of access + decisions + evidence hashes.