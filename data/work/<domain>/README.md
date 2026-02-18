<!--
KFM Governed Artifact
Path: data/work/<domain>/README.md
Purpose: Document the WORK zone expectations and governance boundary for this domain.
-->

# `<domain>` — Work Zone (Intermediate / QA Artifacts)

**Badges:** 🧭 Governed • 🟧 Zone: `work` • 🔒 Fail-Closed • ✅ Source-of-truth: `processed` only

> ⚠️ **NOT PUBLISHABLE / NOT SOURCE-OF-TRUTH**  
> This directory contains **intermediate artifacts** produced by reproducible ETL runs.  
> Only artifacts promoted to `data/processed/<domain>/` **and** described in catalogs are publishable.

---

## Purpose

The **Work Zone** is the controlled staging area between immutable **Raw** inputs and publishable **Processed** outputs.

This folder exists to:

- Validate, normalize, and enrich domain data.
- Produce **run receipts** (`run_record`, `validation_report`, `run_manifest`) required for promotion.
- Support QA, diffs, reproducibility, and auditability.
- Ensure sensitive data is handled with **policy-first** redaction/generalization.

---

## Quick rules

### ✅ Allowed here

- Generated intermediates (`staging/`, `normalized/`, `enriched/`)
- QA exports (`qa/`), diffs for review
- **Receipts** (`run_record.json`, `validation_report.json`, `run_manifest.json`)
- Sanitized logs (no secrets/PII)

### ❌ Not allowed here

- Publishing/serving directly from Work (no “work as truth”)
- Manual edits to generated data (except in `notes/` and only if explicitly governed)
- Secrets, credentials, tokens, API keys
- PII or restricted fields leaking into logs/diffs/receipts

---

## Relationship to other zones

This domain’s data moves through the governed pipeline:

```text
data/
  raw/<domain>/        # immutable source snapshots + manifests + checksums
  work/<domain>/       # THIS FOLDER: intermediate artifacts + run receipts
  processed/<domain>/  # publishable artifacts + checksums
  catalog/             # DCAT/STAC records (publish boundary)
  provenance/          # PROV bundles (lineage boundary)
```

**Trust membrane reminder:** work artifacts are **never** served directly; all access is through the governed API boundary once promoted and cataloged.

---

## Ingestion workflow (raw → work → processed)

This is the standard lifecycle expected for datasets in this domain:

1. **Discover**: resolve endpoints/parameters/auth; cache capability metadata  
2. **Acquire**: fetch incremental slices when possible; otherwise snapshot+diff  
3. **Normalize**: canonical encodings (UTF-8), geometry (WGS84), time (ISO 8601)  
4. **Validate**: schema/geometry/time/license/policy checks  
5. **Enrich**: derive join keys, place/time normalization, entity-resolution candidates  
6. **Publish**: promote to `processed`, update catalogs (DCAT/STAC/PROV), trigger index refresh (search/graph)

> If any gate fails, **fail closed**: stop promotion, emit receipts, and escalate.

---

## Recommended directory layout

```text
data/work/<domain>/
  README.md

  _runs/
    <dataset_slug>/
      <run_id>/                      # e.g., 2026-02-17T14-22-05Z__<spec_hash_short>
        run_record.json
        validation_report.json
        run_manifest.json
        logs/                        # sanitized logs only (no secrets / no PII)
        diffs/                       # optional "what changed" artifacts for PR review
        artifacts/                   # intermediate outputs (may be GC’d per retention policy)

  datasets/
    <dataset_slug>/
      staging/                       # raw→work transforms that are not yet canonical
      normalized/                    # canonical schemas/CRS/time formats
      enriched/                      # derived keys/joins/resolution candidates
      qa/                            # checks, samples, profiles
      exports/                       # candidate outputs prior to promotion
```

**Immutability rule (strongly preferred):** once written, `_runs/<dataset_slug>/<run_id>/` should not be mutated.  
If inputs/spec change → create a new `run_id`.

---

## Run receipts

Promotion to `data/processed/<domain>/` **requires receipts**:

| Receipt | Required | Purpose |
|---|:---:|---|
| `run_record.json` | ✅ | What ran, when, with which inputs/config (`spec_hash`), and status. |
| `validation_report.json` | ✅ | Validation results. Must be PASS to promote. |
| `run_manifest.json` | ✅ | Output inventory + checksums/digests (+ URIs/paths). |

### Suggested (starter) receipt shape

> Update this once the canonical JSON Schemas exist in-repo.

<details>
<summary>Expand: example <code>run_record.json</code> (illustrative)</summary>

```json
{
  "domain": "<domain>",
  "dataset_id": "<dataset_id>",
  "dataset_slug": "<dataset_slug>",
  "run_id": "<run_id>",
  "spec_hash": "<sha256(JCS(spec))>",
  "started_at": "2026-02-17T14:22:05Z",
  "ended_at": "2026-02-17T14:31:42Z",
  "status": "PASS|FAIL",
  "inputs": [
    {"uri": "data/raw/<domain>/<dataset_slug>/...", "sha256": "..."}
  ],
  "outputs": [
    {"uri": "data/work/<domain>/_runs/<dataset_slug>/<run_id>/exports/...", "sha256": "..."}
  ],
  "policy": {
    "policy_label": "public|restricted|sensitive-location|aggregate-only",
    "redactions_applied": true,
    "notes": ""
  }
}
```

</details>

---

## Minimum validation gates

Before promotion, ensure these gates pass (minimum set):

- **Row-level schema validation** (required fields present; type coercion rules documented)
- **Geometry validity + bounds** (no self-intersections; within expected extent when applicable)
- **Temporal consistency** (no future dates for historic archives; no negative durations)
- **License + attribution captured in DCAT**; restrictions encoded in policy
- **Provenance completeness** (every promoted artifact has a PROV chain + deterministic checksum)

> Add domain-specific gates as needed (e.g., topology rules, join-key completeness, drift thresholds).

---

## Sensitivity & redaction

KFM treats sensitivity as **policy-enforced** and **provenance-recorded**.

### Sensitivity classes (recommended)

| Class | Meaning | Typical handling |
|---|---|---|
| `public` | Safe to publish without redaction | Normal publish path |
| `restricted` | Role-based access required | Policy-gated access; redact for public views |
| `sensitive-location` | Coordinates must be generalized/suppressed | Generalize geometry; enforce precision limits; protect exact coordinates |
| `aggregate-only` | Only publish above thresholds | Enforce minimum count/area/time thresholds; publish aggregates only |

### Redaction is a first-class transformation

- Redaction/generalization must be recorded in provenance (PROV).
- Raw stays immutable; redacted derivatives are separate outputs with explicit policy labels.
- Do **not** leak restricted fields/locations in logs, diffs, receipts, or QA exports.

---

## Promotion contract checklist

Promotion from Work → Processed is a **governance boundary**. Do not skip it.

- [ ] `validation_report.json` is PASS
- [ ] Outputs listed in `run_manifest.json` include checksums/digests
- [ ] License + attribution captured (DCAT ready)
- [ ] Sensitivity label set; redaction/generalization applied where required
- [ ] PROV bundle links raw → work → processed
- [ ] (If required) human approval recorded for sensitive triggers
- [ ] Catalog objects validate and cross-link cleanly (DCAT/STAC/PROV)

---

## Operating guidance

### Determinism & reproducibility

- Inputs + spec + toolchain versions should reproduce outputs.
- Never overwrite raw snapshots; always ingest new versions.
- If mapping logic changes, create a new `run_id` (do not mutate prior run folders).

### Retention

Work outputs may be garbage-collected **after**:

- processed artifacts are published and verified, and
- receipts/manifests/provenance are archived (append-only / tamper-evident where supported)

---

## Contacts

- Domain steward: `<name or team>`
- Governance / policy review: `<name or team>`
- Pipeline owner: `<name or team>`

---

## Change log

| Date | Change | Author |
|---|---|---|
| YYYY-MM-DD | Initial template | `<you>` |