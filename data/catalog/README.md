<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8a7a6e8b-0d2e-4a3f-a1c1-7b5a06a5e7c6
title: data/catalog — Catalog Triplet README
type: standard
version: v1
status: draft
owners: kfm-core
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - data/catalog/README.md
tags:
  - kfm
  - catalog
  - dcat
  - stac
  - prov
notes:
  - Defines the “catalog triplet” as a contract surface between pipelines and runtime.
  - Treat as governed documentation: changes can affect validation gates and evidence resolution.
[/KFM_META_BLOCK_V2] -->

# data/catalog — DCAT + STAC + PROV (Catalog Triplet)

Canonical, validated metadata that binds **processed artifacts** to **governed runtime** (API/UI) via deterministic cross-links.

![status](https://img.shields.io/badge/status-draft-yellow)
![scope](https://img.shields.io/badge/scope-catalog%20triplet-blue)
![contracts](https://img.shields.io/badge/contracts-DCAT%20%7C%20STAC%20%7C%20PROV-informational)
![policy](https://img.shields.io/badge/policy_label-public-brightgreen)

## Quick navigation

- [What this directory is](#what-this-directory-is)
- [Directory layout](#directory-layout)
- [Contract surfaces](#contract-surfaces)
- [Profiles](#profiles)
- [EvidenceRef scheme](#evidenceref-scheme)
- [Cross-linking rules](#cross-linking-rules)
- [Time fields](#time-fields)
- [Validation and promotion gates](#validation-and-promotion-gates)
- [Workflow: adding a dataset version](#workflow-adding-a-dataset-version)
- [Definition of Done](#definition-of-done)
- [Appendix: templates](#appendix-templates)

---

## What this directory is

`data/catalog/` is the **catalog + provenance contract surface** for KFM.

It is not “nice metadata.” It is the **canonical interface** between:
- pipeline outputs (artifacts and run receipts), and
- runtime surfaces (catalog browsing, map layers, story citations, Focus Mode evidence).

If a dataset version is “published,” it means:
- artifacts exist (and are checksum-addressed),
- the catalog triplet validates, and
- EvidenceRefs resolve deterministically.

---

## Directory layout

> NOTE: Treat this as the **target shape** for the catalog layer. If your repo organizes these files differently, keep the *contract responsibilities* the same and update this README accordingly.

Proposed layout:
```text
├─ data/
│  ├─ catalog/
│  │  ├─ dcat/                # dataset-level metadata (JSON-LD)
│  │  │  ├─ datasets/
│  │  │  └─ distributions/
│  │  ├─ stac/                # asset-level metadata (JSON)
│  │  │  ├─ catalog.json
│  │  │  ├─ collections/
│  │  │  └─ items/
│  │  ├─ prov/                # lineage bundles (JSON-LD / PROV-JSON)
│  │  │  ├─ runs/
│  │  │  └─ bundles/
│  │  ├─ schemas/             # JSON Schema / SHACL profiles (validators consume these)
│  │  ├─ reports/             # validator output (link-check, schema check, counts)
│  │  └─ README.md            # you are here
```
---

## Contract surfaces

| Surface | Primary question answered | Scope | Must include |
|---|---|---|---|
| **DCAT** | “What is this dataset? Who published it? What’s the license? What are the distributions?” | Dataset-level | Title/description/publisher/license, coverage, distributions, policy label, dataset_id + dataset_version_id, link to PROV |
| **STAC** | “What assets exist? What are their spatiotemporal extents? Where are the files?” | Asset-level | Collections/items/assets, extents, checksums, links to DCAT and PROV/run receipts, policy-consistent geometry |
| **PROV** | “How were outputs created? Which inputs/tools/params?” | Lineage | Activity per run, Entity per artifact, Agent for pipeline + approvals, environment capture, policy decision references |

---

## Profiles

KFM treats DCAT/STAC/PROV as **profiled contracts**: validation should be strict and predictable.

### Minimal required fields

**DCAT dataset record (minimum):**
- `dct:title`
- `dct:description`
- `dct:publisher`
- `dct:license` (or `dct:rights`)
- `dcat:theme` (controlled vocabulary)
- `dct:spatial` and `dct:temporal` coverage
- `dcat:distribution` (one per artifact class)
- `prov:wasGeneratedBy` → link to PROV activity bundle
- `kfm:policy_label`
- `kfm:dataset_id`
- `kfm:dataset_version_id`

**STAC collection (minimum):**
- `id`, `title`, `description`
- `extent` (spatial bbox + temporal interval)
- `license`
- link to DCAT record (`rel="describedby"` recommended)
- `kfm:dataset_version_id`
- policy label

**STAC item (minimum):**
- `id`
- `geometry` or `bbox` (must be policy-consistent; generalized if needed)
- `datetime` or `start_datetime`/`end_datetime`
- `assets` with `href` + checksum + `media_type`
- links to:
  - PROV activity/run receipt
  - DCAT distribution

**PROV bundle (minimum):**
- `prov:Activity` per pipeline run
- `prov:Entity` per artifact (raw/work/processed)
- `prov:Agent` for pipeline and steward approval events
- `prov:used` and `prov:wasGeneratedBy` edges
- `kfm:policy_decision` references (decision_id + obligations)
- environment capture (container digest, git commit, parameters)

---

## EvidenceRef scheme

Evidence resolution must not “guess.”

EvidenceRefs are stable references such as:
- `dcat://...` → dataset/distribution metadata
- `stac://...` → collection/item/asset metadata
- `prov://...` → run lineage (activities/entities/agents)
- `doc://...` → governed docs / story citations
- `graph://...` → entity relations (if enabled)

**Resolver contract (behavioral):**
- Accepts an EvidenceRef (`scheme://...`) *or* a structured reference (dataset_version + record_id + span)
- Applies policy and returns allow/deny + obligations
- Returns an EvidenceBundle with:
  - human view (renderable card)
  - machine metadata (JSON)
  - artifact links (only if allowed)
  - digests + dataset_version ids
  - audit references
- Must be usable in **≤ 2 calls** from the UI (feature click or citation click → resolve → view)

---

## Cross-linking rules

Cross-links make navigation deterministic and testable:

- DCAT dataset → `dcat:distribution` → artifact digests
- DCAT dataset → `prov:wasGeneratedBy` → PROV bundle
- STAC collection → `rel="describedby"` → DCAT dataset
- STAC item → link to PROV activity and/or run receipt
- STAC item → link to DCAT distribution

**Rule of thumb:** if a human can’t jump from “map feature → evidence → lineage → artifact” without manual searching, the catalog is incomplete.

---

## Time fields

KFM commonly needs more than one time axis:

- **Event time:** when something happened (the thing you usually want to filter on in the map timeline).
- **Transaction time:** when KFM acquired/published the record.
- **Valid time (optional):** when a statement is considered true (useful for boundary changes and administrative history).

Catalog records SHOULD make it explicit which time axis each field represents.

---

## Validation and promotion gates

Catalog triplet validation is a **fail-closed promotion gate**.

### Promotion gates (minimum)

| Gate | Fail-closed check (summary) |
|---|---|
| **A — Identity & versioning** | Stable Dataset ID; DatasetVersion ID immutable and derived from stable spec hash |
| **B — Licensing & rights** | Explicit license + rights holder/attribution captured; unclear licensing stays quarantined |
| **C — Sensitivity & redaction plan** | policy_label assigned; redaction/generalization plan exists and is recorded in PROV |
| **D — Catalog triplet validation** | DCAT validates; STAC validates; PROV validates; cross-links present and resolvable |
| **E — Run receipt & checksums** | run_receipt exists; inputs/outputs enumerated with checksums; environment captured |
| **F — Policy + contract tests** | Policy tests pass; evidence resolver can resolve at least one EvidenceRef in CI; schemas validate |
| **G — Optional but recommended** | SBOM/build provenance; perf smoke checks; basic accessibility smoke checks |

---

## Workflow: adding a dataset version

This is the smallest credible “happy path” for adding data that will appear in map/story/focus surfaces.

1. **Acquire to RAW**
   - Capture acquisition manifest (source, time fetched, terms snapshot)
   - Store raw artifact(s) immutable; compute checksums

2. **Transform in WORK / QUARANTINE**
   - Normalize formats
   - Produce QA reports
   - If license/sensitivity is unclear → quarantine and stop

3. **Write PROCESSED artifacts**
   - Output in KFM-approved formats
   - Ensure every artifact is digest-addressed (or at least checksum-recorded)

4. **Emit catalog triplet**
   - DCAT dataset + distributions that reference artifact digests
   - STAC collection + items (if spatiotemporal) with policy-consistent geometry and checksums
   - PROV bundle linking inputs → activity → outputs, including environment and policy decision refs

5. **Emit run receipt**
   - One per producing run (ingest, transform, publish)
   - Must list inputs, outputs, environment, validation results, policy decision reference

6. **Validate + link-check**
   - Schema validation for DCAT/STAC/PROV profiles
   - Link integrity across the triplet
   - Evidence resolver contract test(s)

7. **Promote**
   - Only after all required gates pass
   - Record changelog: what changed, why, and what it affects

---

## Definition of Done

A dataset integration is DONE only when:

- [ ] RAW acquisition is reproducible and documented
- [ ] WORK transforms are deterministic (same inputs → same outputs; same spec → same hash)
- [ ] PROCESSED artifacts exist in approved formats and are digest/checksum-addressed
- [ ] Catalog triplet validates and is cross-linked
- [ ] EvidenceRefs resolve and render in the UI evidence drawer (or equivalent consumer)
- [ ] policy_label assigned, with documented review/approval
- [ ] Changelog entry explains what changed and why

---

## Appendix: templates

> These are intentionally minimal sketches to help contributors understand intent.
> Use the project’s schemas/profiles as the actual source of truth.

### DCAT dataset record (sketch)

~~~json
{
  "@type": "dcat:Dataset",
  "dct:title": "Example dataset title",
  "dct:description": "What this is and why it exists.",
  "dct:publisher": {"@id": "kfm://agent/example_publisher"},
  "dct:license": "CC-BY-4.0",
  "dcat:theme": ["kfm:theme/example"],
  "dct:spatial": "kfm:spatial/kansas",
  "dct:temporal": {"start": "1854-01-01", "end": "1900-12-31"},
  "kfm:policy_label": "public",
  "kfm:dataset_id": "kfm://dataset/example_dataset",
  "kfm:dataset_version_id": "kfm://dataset/@example_dataset/2026-02.abcd1234",
  "dcat:distribution": [
    {
      "@type": "dcat:Distribution",
      "dcat:mediaType": "application/x-parquet",
      "kfm:artifact_digest": "sha256:..."
    }
  ],
  "prov:wasGeneratedBy": {"@id": "kfm://run/2026-02-20T12:00:00Z.abcd"}
}
~~~

### STAC item (sketch)

~~~json
{
  "type": "Feature",
  "stac_version": "1.0.0",
  "id": "example_item_id",
  "properties": {
    "datetime": "2026-02-19T00:00:00Z",
    "kfm:dataset_version_id": "kfm://dataset/@example_dataset/2026-02.abcd1234",
    "kfm:policy_label": "public"
  },
  "geometry": null,
  "bbox": [-102.0, 36.9, -94.6, 40.0],
  "assets": {
    "data": {
      "href": "data/processed/example.parquet",
      "type": "application/x-parquet",
      "checksum:sha256": "..."
    }
  },
  "links": [
    {"rel": "describedby", "href": "../dcat/datasets/example_dataset.jsonld"},
    {"rel": "provenance", "href": "../prov/runs/2026-02-20T12:00:00Z.abcd.jsonld"}
  ]
}
~~~

### Run receipt (sketch)

~~~json
{
  "run_id": "kfm://run/2026-02-20T12:00:00Z.abcd",
  "actor": {"principal": "svc:pipeline", "role": "pipeline"},
  "operation": "ingest+publish",
  "dataset_version_id": "kfm://dataset/@example_dataset/2026-02.abcd1234",
  "inputs": [{"uri": "raw/source.csv", "digest": "sha256:..."}],
  "outputs": [{"uri": "processed/example.parquet", "digest": "sha256:..."}],
  "environment": {
    "container_digest": "sha256:...",
    "git_commit": "deadbeef",
    "params_digest": "sha256:..."
  },
  "validation": {"status": "pass", "report_digest": "sha256:..."},
  "policy": {"decision_id": "kfm://policy_decision/xyz"},
  "created_at": "2026-02-20T12:05:00Z"
}
~~~

---

_Back to top: [Quick navigation](#quick-navigation)
