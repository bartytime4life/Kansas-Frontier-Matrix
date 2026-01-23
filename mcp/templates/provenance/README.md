# 🧾 Provenance Template Pack (MCP)

![Provenance-First](https://img.shields.io/badge/provenance-first-2ea44f)
![STAC](https://img.shields.io/badge/STAC-cataloged-6f42c1)
![DCAT](https://img.shields.io/badge/DCAT-cataloged-f39c12)
![W3C PROV](https://img.shields.io/badge/W3C-PROV--O-1f77b4)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-governed-0b7285)
![Policy%20as%20Code](https://img.shields.io/badge/OPA%2FRego-policy%20gates-555)

**Path:** `mcp/templates/provenance/`

> [!IMPORTANT]
> **No mystery layers. No unsourced outputs.**  
> If something is visible in the UI, queryable via the API, or exportable as an artifact (dataset, layer, Story Node, Pulse Thread, Focus Mode answer), it must have **machine‑readable provenance**.

---

## 📌 What this folder is

This folder defines **canonical provenance templates** used across the Kansas Matrix / Kansas Frontier Matrix ecosystem to ensure:

- ✅ **Reproducibility** (same inputs + same config ⇒ same outputs)
- 🔍 **Traceability** (every claim/layer/output can be walked back to evidence)
- 🧭 **Governance** (FAIR + CARE compliance via policy gates)
- 🧑‍⚖️ **Human-in-the-loop** review for anything that impacts public understanding or sensitive domains
- 🗺️ **User-visible provenance** (the UI can explain “what am I looking at?” at any time)

These templates turn provenance into a **first-class product artifact**, not an afterthought.

---

## 🧠 The core pattern: “Evidence Triplet” (plus supply-chain extras)

KFM’s baseline publishing contract is the **triplet**:

1. 🛰️ **STAC** – spatial/temporal footprint + assets (tiles, rasters, vectors, docs)
2. 🗂️ **DCAT** – dataset publication metadata (title, license, publisher, access)
3. 🔗 **PROV** – lineage graph (inputs → activities → outputs, with agents)

Optional but strongly recommended for large binaries & distribution:

4. 📦 **OCI distribution** – store artifacts (PMTiles, GeoParquet, COGs) in an OCI registry
5. 🔏 **Signatures / attestations** – Cosign signatures, SBOMs, and provenance attachments

---

## 🧱 Where rendered outputs should land

> [!NOTE]
> Exact folder names may differ slightly per repo, but the *boundary artifacts* land in canonical locations.

```text
📦 data/
├─ 🧾 raw/                # immutable “as received” evidence
├─ 🛠️ work/               # intermediate transforms (reproducible, throwaway)
├─ ✅ processed/           # publishable outputs (COGs, PMTiles, GeoParquet, etc.)
├─ 🛰️ stac/               # STAC Items/Collections (asset + spatial/temporal)
├─ 🗂️ catalog/
│  └─ dcat/               # DCAT dataset records (license/publisher/access)
├─ 🔗 prov/               # PROV JSON-LD bundles (lineage)
└─ 🧪 audits/             # run manifests, logs, idempotency keys, digests
```

---

## 🧬 Provenance primitives (how to think)

| Primitive | Meaning | Examples |
|---|---|---|
| **Entity** 📄 | A thing (input/output) | raw download, processed PMTiles, GeoParquet, OCR corpus, generated report |
| **Activity** ⚙️ | A transformation/event | ETL run, reprojection, georeference, join, model inference, PR merge |
| **Agent** 🧑‍💻🤖 | Who/what acted | maintainer, CI runner, automation bot, model runtime |

> [!TIP]
> If you can’t name the **Entity**, **Activity**, and **Agent**, you don’t have enough provenance yet.

---

## 🧩 Template catalog (recommended)

This README is the contract; the templates are the implementation. A typical pack looks like:

```text
mcp/templates/provenance/
├─ 📄 README.md                           # 📘 How to use provenance templates + required inputs/outputs + validation steps
├─ 🧬 prov/                               # 🧬 PROV template files (Jinja) for generating JSON-LD provenance bundles
│  ├─ 🧬🧾 dataset.prov.jsonld.jinja       # Dataset lineage template (sources → transforms → published artifacts)
│  ├─ 🧬🧾 pipeline_run.prov.jsonld.jinja  # Pipeline run template (activities/agents/entities + params + timestamps)
│  ├─ 🧬🧾 focus_answer.prov.jsonld.jinja  # Focus Mode answer provenance (retrieval → reasoning steps → cited outputs)
│  └─ 🧬🧾 github_pr.prov.jsonld.jinja     # PR→PROV template (commits/reviews → artifacts/receipts/approvals)
├─ 🧾 manifests/                          # 🧾 Non-PROV manifest templates (receipts + evidence indices)
│  ├─ 🧾🔐 run_manifest.json.jinja         # Run manifest template (commands, env, inputs/outputs, digests, tool versions)
│  └─ 📎🧾 story_evidence.yml.jinja        # Story evidence manifest template (claims→citations→artifacts + checksums)
├─ 🧠 contexts/                           # 🧠 JSON-LD contexts used by the generated PROV bundles
│  └─ 🧠🧬 kfm.context.jsonld              # KFM @context (namespaces, term mappings, prefixes; used by templates)
└─ ✅ policy/                             # ✅ Policy pack enforcing template outputs (schema/profile invariants)
   ├─ ⚖️📄 provenance.rego                 # OPA/Rego rules for provenance artifacts (required links, ids, ordering, etc.)
   └─ ⚙️📄 conftest.toml                   # Conftest configuration for running provenance.rego against generated outputs
```

> [!NOTE]
> Use whatever renderer your repo standardizes on (Jinja/Cookiecutter/etc.). The important part is that the output conforms to the profiles + gates.

---

## 🛠️ How to use these templates

### 1) Add or update a dataset (batch / “static”)

✅ **Goal:** produce publishable data **and** the evidence triplet.

**Workflow:**
1. 🧾 Put source bytes in `data/raw/<domain>/...` (**immutable**)
2. 🛠️ Run ETL into `data/processed/<domain>/...`
3. 🛰️ Generate STAC (Collection + Item(s)) for assets
4. 🗂️ Generate DCAT dataset record (license/publisher/access)
5. 🔗 Generate PROV bundle capturing:
   - input entities (raw bytes, upstream datasets)
   - activity (pipeline run; config; tool versions)
   - output entities (processed artifacts + digests)
6. 🧪 Emit a **Run Manifest** (audit trail) and store it under `data/audits/<run_id>/...`
7. ✅ Pass policy gates (schema + OPA/Conftest) → open PR → review → merge

---

### 2) Record a pipeline run (Run Manifest + PROV)

A pipeline run must be independently audit-able.

**Run Manifest should capture (minimum):**
- `run_id`, `run_time`
- `idempotency_key` (so reruns can be recognized)
- `canonical_digest` (hash of canonicalized manifest JSON)
- `source_urls` / `dataset_ids` used
- `tool_versions` (GDAL, Python, PostGIS, etc.)
- `summary_counts` and error summaries

> [!IMPORTANT]
> Treat the Run Manifest as “the electronic lab notebook entry” for the run. It should be usable for reproduction *even years later*.

---

### 3) Distribute large artifacts (OCI + ORAS + Cosign)

When artifacts are too large for Git, store them in an OCI registry:

- 📦 Use **ORAS** to push arbitrary data files (PMTiles, GeoParquet, COGs) with custom media types.
- 🔏 Use **Cosign** to sign the artifact manifest (keyless/OIDC is ideal for CI).
- 🔗 Attach provenance / SBOM as **OCI referrers** (linked to the digest).

#### Template snippet: `distribution.oci` (YAML-ish)

```yaml
distribution:
  oci:
    registry: ghcr.io
    repository: myorg/kfm/surficial_geology
    tag: "20260111"
    digest: "sha256:PUT_REAL_DIGEST_HERE"
    artifacts:
      - name: surficial_geology.pmtiles
        mediaType: application/vnd.pmtiles
      - name: surficial_geology.parquet
        mediaType: application/vnd.geo+parquet
    provenance_ref:
      type: oci-referrer
      selector: "sha256:PUT_REAL_DIGEST_HERE"
    verification:
      signatures:
        tool: cosign
        mode: keyless
        issuer: oidc
```

> [!TIP]
> Catalog records (STAC/DCAT) should reference OCI artifacts by **digest**, not only “latest” tags.

---

### 4) Author a Story Node / Pulse Thread (Evidence Manifest + lineage)

Narrative content is only trusted if it’s **evidence-backed**.

**Required:**
- 🧾 `story_evidence.yml` listing sources (dataset IDs, URLs, snapshots)
- 🔗 (recommended) a PROV bundle connecting the Story/Pulse to the evidence entities and authoring activity

#### Example: evidence manifest (shape)

```yaml
story_id: kfm:story:example:001
title: "Example Narrative"
created_at: "2026-01-21T00:00:00Z"
claims:
  - id: claim-001
    text: "A specific claim that must be verifiable."
    evidence:
      - kind: dataset
        dataset_id: kfm:dataset:hydro:usgs_nwis:v1
        locator: "station_id=06891000&timestamp=2026-01-21T20:00:00Z"
      - kind: document
        source_url: "https://example.org/report.pdf"
        checksum: "sha256:..."
```

> [!WARNING]
> **CI should fail** if a citation in a Story/Pulse cannot be resolved to an evidence manifest entry.

---

### 5) Log Focus Mode / AI outputs (answer provenance)

Focus Mode answers must be **explainable** and **traceable**:

- Every answer should cite what it used (datasets, queries, docs).
- AI outputs and key decisions should be recorded in an **append-only governance ledger**.
- For dynamic queries (real-time), provenance must include the **timestamped reading** used as an input entity.

✅ Template should capture (minimum):
- question + answer ID
- timestamp
- model/runtime ID and version
- source dataset IDs + citations
- query parameters (when applicable)
- policy gate outcomes (passed/blocked/warn)

---

### 6) Treat DevOps as provenance (GitHub PR → PROV)

Provenance doesn’t stop at data. PRs and releases are **Activities** too.

A PR-to-PROV template should represent:
- **Entities:** commit(s), files changed, generated artifacts
- **Activity:** “PR merged”, “pipeline publish”
- **Agents:** author(s), reviewer(s), CI bot

This makes “how did this dataset get here?” answerable directly from the graph.

---

## ✅ Validation & policy gates (fail-closed by default)

This system assumes **policy-as-code**:

- JSON Schema validation (STAC/DCAT/PROV + domain contracts)
- OPA/Rego rules via Conftest
- Secrets scanning & restricted fields
- Required license/provider fields
- Sensitivity classification and redaction rules
- Citation completeness (stories + AI)

> [!IMPORTANT]
> Gates must be **fail-closed**: missing metadata, missing provenance, or invalid schema blocks merges.

---

## 🗺️ UI + API expectations (why provenance is user-facing)

Provenance isn’t just for maintainers—KFM’s UI is designed to surface it:

- 🧾 **Layer provenance panel**: active layers + sources + processing summary
- 🧠 **Focus Mode citations**: “every insight has a footnote”
- 📤 **Exports carry credits**: attributions bundled into downloadable artifacts
- 🔒 **Classification enforcement**: API filters or labels sensitive features

---

## 🔢 Versioning rules & identifiers

To keep lineage stable:

- Use stable dataset IDs and versioning (semver or date tags)
- Prefer **content digests** (sha256) for immutable identity of files
- Record tool versions and environment snapshots (requirements/containers)
- Never overwrite raw data; any change must be a new entity + activity

> [!TIP]
> If you can’t reproduce the output from recorded inputs + config, the provenance is incomplete.

---

## 🧪 Minimal PROV JSON‑LD example (illustrative)

<details>
  <summary>Click to expand</summary>

```json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    "./contexts/kfm.context.jsonld"
  ],
  "id": "kfm:prov:bundle:run:2026-01-21T20:00:00Z",
  "type": "prov:Bundle",
  "entity": {
    "kfm:entity:raw:usgs_nwis_snapshot_2026-01-21.json": {
      "prov:label": "USGS NWIS snapshot",
      "kfm:checksum": "sha256:..."
    },
    "kfm:entity:processed:river_gauges.parquet": {
      "prov:label": "River gauges (normalized)",
      "kfm:checksum": "sha256:..."
    }
  },
  "activity": {
    "kfm:activity:pipeline:hydro_ingest:run:RUN_ID": {
      "prov:used": ["kfm:entity:raw:usgs_nwis_snapshot_2026-01-21.json"],
      "prov:generated": ["kfm:entity:processed:river_gauges.parquet"],
      "kfm:code_commit": "GIT_SHA",
      "kfm:tool_versions": {
        "python": "3.x",
        "gdal": "x.y",
        "postgis": "x.y"
      }
    }
  },
  "agent": {
    "kfm:agent:ci:github_actions": {
      "prov:type": "prov:SoftwareAgent",
      "prov:label": "GitHub Actions"
    }
  }
}
```

</details>

---

## ✅ Definition of Done (DoD) checklist

Use this when adding any dataset, derived artifact, story, or AI output:

- [ ] 🧾 Raw evidence stored immutably (or referenced immutably)
- [ ] 🛠️ Processing is deterministic (config/code; no manual edits)
- [ ] 🛰️ STAC records exist and validate
- [ ] 🗂️ DCAT record exists and validates (license + publisher present)
- [ ] 🔗 PROV lineage exists and validates (entities/activities/agents linked)
- [ ] 🧪 Run Manifest emitted with canonical digest
- [ ] 📦 (If OCI) distribution references include digest + media types
- [ ] 🔏 (If OCI) artifact signatures/attestations are present
- [ ] 🧠 (If AI/story) citations resolve to evidence manifest entries
- [ ] ✅ All policy gates pass (fail-closed)

---

## 🤝 Contributing

If you add a new provenance pattern:

1. Copy the closest existing template (don’t invent one-off formats)
2. Extend profiles intentionally (avoid ad-hoc fields)
3. Add/adjust policy gates so the pattern stays enforceable
4. Add an example fixture for CI validation (recommended)

> [!NOTE]
> Provenance isn’t bureaucracy—it’s the trust engine that keeps KFM credible.
