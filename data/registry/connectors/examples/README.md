# 🔌 Connector Examples

![Governed](https://img.shields.io/badge/governed-yes-blue)
![Evidence First](https://img.shields.io/badge/evidence--first-required-brightgreen)
![Fail Closed](https://img.shields.io/badge/posture-fail--closed-red)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-7a3df0)

This folder contains **example connector packages** for the Kansas Frontier Matrix (KFM) data plane.

The goal is to make it easy to add new sources **without reinventing** the same scaffolding each time:
**connector → pipeline → validation gates → catalogs → provenance → promotion**.

> [!IMPORTANT]
> **Examples are not production ingestion.**
> - Use **synthetic fixtures** or **tiny public slices**.
> - **Never commit secrets** (keys/tokens) or restricted raw data.
> - If a source can include sensitive locations or small-area re-identification risk, default to `restricted` and require redaction/aggregation gates before anything public.

---

## What belongs here

This directory should hold **small, reviewable, offline-friendly** examples that demonstrate the “golden path”:

- A connector registry entry with reasonable defaults (schedule, incremental strategy, auth posture, policy label).
- A dataset-family scaffold (`pipeline.yaml`, `schemas/`, `qa/`, and catalog/provenance templates).
- Fixtures and expected outputs to support deterministic CI.

The “predictable artifact set” pattern is intentionally consistent across dataset families:
`pipeline.yaml + schemas + qa + stac + dcat + prov + graph` [oai_citation:1‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

---

## Concepts

### Connector

A **connector** acquires upstream data into the **Raw zone** and emits evidence artifacts:

- **Deterministic manifest + checksums**
- Metadata needed for policy and provenance
- Enough context to support downstream normalization and cataloging [oai_citation:2‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

### Watcher

A **watcher** is the change detector that decides *when* to run (or open a PR). Prefer cheap HTTP signals like **ETag / Last-Modified** when available. [oai_citation:3‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

### Pipeline

A pipeline is the deterministic promotion workflow. The blueprint describes a standard progression:

- Discover → Acquire → Normalize → Validate → Enrich → Publish [oai_citation:4‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

(You may also see this summarized as a promotion saga: Discover → Fetch → Normalize → Validate → Publish → Catalog.) [oai_citation:5‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

---

## Directory layout

Each example lives in its own folder named by `connector_id`.

```text
data/registry/connectors/examples/
  <connector_id>/
    README.md
    connector.yaml
    pipeline.yaml
    schemas/
    qa/
    dcat/
    stac/
    prov/
    graph/              # optional (only if graph-ingested)
    fixtures/
      raw/              # tiny public slice or synthetic input
    expected/
      work/
      processed/
      catalogs/
      prov/
```

### Folder responsibilities

| Path | Purpose | Notes |
|---|---|---|
| `connector.yaml` | Connector registry entry | No secrets. Auth config must reference vault/secret names, never literal values. |
| `pipeline.yaml` | Dataset-family contract | Inputs/outputs/resources/schedules. |
| `schemas/` | Canonical mapping schemas | Keeps normalization explicit + testable. |
| `qa/` | Validation + drift thresholds | CI should run these on fixtures. |
| `dcat/` | DCAT dataset/distribution templates | DCAT is “always” in DoD for promotion. |
| `stac/` | STAC collection/item templates | Use when you publish spatial assets or map layers. |
| `prov/` | PROV templates + example run outputs | Every promoted artifact should be traceable. |
| `graph/` | Graph mapping rules | Optional; only if this dataset family is graph-ingested. |
| `fixtures/` | Inputs for offline tests | Prefer deterministic, small slices. |
| `expected/` | Golden outputs | Used by integration tests to detect drift. |

---

## Connector registry fields

The integration blueprint’s “recommended defaults” commonly include these keys:

| Key | Purpose | Recommended rule of thumb |
|---|---|---|
| `schedule` | Intended run cadence | Match source volatility (hourly, daily, static, etc.). [oai_citation:6‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |
| `incremental_cursor` | Incremental ingestion strategy | Prefer `modified_date/eventDate/publicationDate`; otherwise snapshot+diff. [oai_citation:7‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |
| `auth` | Authentication posture | Default none for public; otherwise **vault-managed secrets** and never committed. [oai_citation:8‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |
| `rate_limit` | Provider respect + retries | Respect upstream limits; exponential backoff; cache common queries. [oai_citation:9‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |
| `format_targets` | Intended output formats | JSON/CSV (tabular), GeoJSON/Parquet (vector), COG (raster), PDF/JPEG/PNG (artifacts). [oai_citation:10‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |
| `policy_label` | Exposure label | `public` / `restricted` / `sensitive-location` (sometimes per record). [oai_citation:11‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea) |

> [!NOTE]
> This folder documents **field intent**, not a final schema. If your repo has a JSON Schema for connector entries, treat that as source-of-truth and update examples to match.

---

## Ingestion workflow

```mermaid
flowchart LR
  Discover --> Acquire --> Normalize --> Validate --> Enrich --> Publish --> Catalog
```

- **Discover:** resolve endpoints, params, auth needs; cache capability metadata. [oai_citation:12‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Acquire:** fetch incrementally if possible; else snapshot and diff. [oai_citation:13‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Normalize:** canonical encodings (UTF-8), geometry (WGS84), time (ISO 8601). [oai_citation:14‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Validate:** schema, geometry, timestamp sanity, license/policy checks. [oai_citation:15‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Enrich:** derive join keys (GeoIDs), place/time normalization, entity resolution candidates. [oai_citation:16‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Publish:** promote to Processed; update catalogs and trigger index refresh. [oai_citation:17‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Minimum validation gates

These gates should be implementable in CI and run on fixtures:

- Row-level schema validation (required fields present; documented coercion rules). [oai_citation:18‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- Geometry validity + bounds (no self-intersections; inside expected extent when applicable). [oai_citation:19‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- Temporal consistency (no future dates for historic archives; no negative durations). [oai_citation:20‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- License + attribution captured in DCAT; restrictions encoded in policy. [oai_citation:21‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- Provenance completeness: every promoted artifact has a PROV chain and deterministic checksum. [oai_citation:22‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Test plan template

A CI-ready test plan pattern:

- **Unit:** schema mapping/type coercion; geometry helpers; incremental window logic. [oai_citation:23‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Integration:** run connector on a fixed small slice; assert stable checksums + counts. [oai_citation:24‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Contract:** verify API response includes provenance bundle and respects policy redaction. [oai_citation:25‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- **Regression:** profiling metrics are stable or explainably versioned. [oai_citation:26‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Definition of Done for a new example

Use this checklist for each new folder under `examples/`:

- [ ] Connector entry exists and is registered in the data-source registry config. [oai_citation:27‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Raw acquisition produces deterministic manifest + checksums. [oai_citation:28‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Normalization emits canonical schema and/or STAC assets. [oai_citation:29‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Validation gates implemented and enforced in CI. [oai_citation:30‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Policy labels defined; restricted fields/locations are redacted per rules. [oai_citation:31‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Catalogs emitted (DCAT always; STAC/PROV as applicable) and link-check clean. [oai_citation:32‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] API contract tests pass for at least one representative query. [oai_citation:33‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)
- [ ] Backfill strategy documented (ranges + expected runtime). [oai_citation:34‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Canonical mapping and ID rules

Minimum canonical mapping expectations:

- Persist an upstream dataset identifier as `dataset_id + upstream_id`.
- Treat the dataset version as a **content-hash of the raw manifest**.
- Require a stable `source_record_id` per upstream semantics for evidence citation and replay safety. [oai_citation:35‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

---

## Security and governance

### Zero-trust ingest pattern

When examples include acquisition logic, follow a hardened intake posture:

- Short-lived credentials (no long-lived secrets in repo)
- Signed request/response logs
- Content-addressed staging (digest-keyed immutability)
- License-first gates and attestations [oai_citation:36‡KFM-Bluprint-&-Ideas.pdf](sediment://file_000000004e9c71f598d3d784f6a13c46)

### Sensitivity and redaction

The integration blueprint explicitly calls out sensitivity classes and treating redaction as a first-class transformation (implemented as policy + gates). [oai_citation:37‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

> [!WARNING]
> If an example involves cultural heritage sites, private individuals, or location-sensitive resources:
> - **Generalize** geometry and time precision by default.
> - Use `policy_label: restricted` or `policy_label: sensitive-location`.
> - Require a redaction/aggregation gate before promotion.

---

## Catalog templates

Use these sections as “minimum field” checklists when writing example templates.

<details>
<summary><strong>DCAT minimum fields</strong></summary>

From the blueprint’s catalog template appendix:
- `dct:title`, `dct:description`
- `dct:publisher`
- `dct:license`
- `dct:spatial`, `dct:temporal`
- `dct:accrualPeriodicity`
- `dcat:distribution`
- `prov:wasGeneratedBy` (link to PROV activity) [oai_citation:38‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

</details>

<details>
<summary><strong>STAC minimum fields</strong></summary>

From the blueprint’s catalog template appendix:
- Collection: `id`, `title`, `description`, `license`, `extent.spatial`, `extent.temporal`, `providers`
- Item: `id`, `geometry`, `bbox`, `datetime`, `assets`, `links` (incl. derived/provenance link) [oai_citation:39‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

</details>

<details>
<summary><strong>PROV minimum fields</strong></summary>

From the blueprint’s catalog template appendix:
- Entities: raw asset, normalized table, derived artifact
- Activities: ingest run, transform, redaction
- Agents: connector/service, steward approval
- Relations: `wasGeneratedBy`, `used`, `wasDerivedFrom`, `wasAssociatedWith` [oai_citation:40‡KFM_Comprehensive_Data_Source_Integration_Blueprint_v1_massive.pdf](sediment://file_000000000bbc722f8debeb7985ab63ea)

</details>

---

## Example snippets

These snippets are illustrative and intended to show the **shape** of an example entry.

### `connector.yaml`

```yaml
connector_id: example.source
name: Example Source Connector
domain: example-domain

schedule: daily
incremental_cursor:
  strategy: modified_date   # or eventDate/publicationDate; else snapshot+diff
auth:
  type: none                # if not none: reference vault secret name, do not embed tokens
rate_limit:
  strategy: respect_upstream
format_targets:
  - json
  - parquet
policy_label: restricted     # public | restricted | sensitive-location

outputs:
  raw_zone: raw
  processed_zone: processed
```

### `pipeline.yaml`

```yaml
pipeline_id: example.source.v1
inputs:
  - connector_id: example.source
    zone: raw
outputs:
  - zone: processed
    catalogs: [dcat, prov]
    stac: optional
resources:
  cpu: "1"
  memory: "2Gi"
```

---

## Contributing

- Keep examples **small** and **reviewable**.
- Prefer fixtures that are deterministic and safe to distribute.
- When in doubt, choose the stricter policy label and document why.

---

## Sources

This README is aligned to the following internal KFM design artifacts:

- **Kansas Frontier Matrix (KFM) – Data Source Integration Blueprint** — Version 1.0 (2026-02-12)  
  Sections used: ingestion workflow, validation gates, DoD, connector configuration defaults, catalog templates.
- **KFM Pulse → Integration Kit** — Generated (2026-02-15)  
  Sections used: minimal pipeline blueprint contract, zero-trust ingest, CI-enforceable invariants.