<!--
📄 TEMPLATE__PROVENANCE_ATTESTATION.md
📍 Intended path: mcp/templates/provenance/TEMPLATE__PROVENANCE_ATTESTATION.md

✅ Purpose:
Evidence-first provenance + governance + supply-chain attestation for **any KFM artifact**
(datasets, layers, Story Nodes, Pulse Threads, simulations, AI answers, exports, registries, graph updates).

🧠 Guiding principle:
If a reviewer can’t reproduce (or at least *audit*) the artifact from what’s recorded here, it’s not “done”.

🛡️ Policy mindset:
“Provenance-first publishing” → publish **STAC + DCAT + PROV + manifests** before the artifact is promoted
into graph/UI, exported, or treated as “trusted”.
-->

# TEMPLATE — Provenance Attestation ⛓️🧾

![Provenance First](https://img.shields.io/badge/Provenance-first-2ea44f)
![Evidence](https://img.shields.io/badge/Evidence-backed-blue)
![FAIR+CARE](https://img.shields.io/badge/FAIR%20%2B%20CARE-aligned-purple)
![STAC](https://img.shields.io/badge/STAC-profile-5c2d91)
![DCAT](https://img.shields.io/badge/DCAT-catalog-0b7285)
![W3C PROV](https://img.shields.io/badge/PROV-O-lineage-1c7ed6)
![SLSA](https://img.shields.io/badge/SLSA-attestable-black)
![Cosign](https://img.shields.io/badge/Sigstore-cosign-orange)

> 🧭 **KFM Rule:** “No mystery layers.” Every layer, story, model output, or export must have a clear lineage trail (inputs → transforms → outputs) and enforceable governance metadata. 🗺️🔍

---

## 📌 Quick Start

1. **Copy** this template into the artifact’s provenance location (recommended: `data/prov/` or alongside the artifact in `data/processed/...`).  
2. Fill all **Required ✅** fields. If N/A, write `N/A (why)`.  
3. Attach/commit required manifests & metadata (**source.json**, **checksums.sha256**, STAC/DCAT/PROV refs, run manifests).  
4. Ensure **policy gates** pass (schema, licensing, sensitivity, citations, provenance completeness).  
5. Add reviewer sign-off (human/CI) and (if applicable) **cosign / in-toto** references.

---

## 🧩 Attestation Type

> Pick the closest type (you can combine, but call out the primary).

- [ ] **dataset_ingestion** (raw → curated)
- [ ] **dataset_transform** (curated → derived)
- [ ] **layer_publish** (processed → map layer / tileset)
- [ ] **graph_update** (knowledge graph mutation/import)
- [ ] **story_node** (narrative, timeline, annotated claims)
- [ ] **pulse_thread** (discussion → decision → action)
- [ ] **simulation_run** (model run, scenario, forecast)
- [ ] **ai_answer / focus_mode** (assistant output & context bundle)
- [ ] **export_package** (offline pack, PDF, report, share bundle)
- [ ] **registry_publish** (OCI artifact publish + signatures)

---

## ✅ Minimum Completeness Gates

### Required for *all* attestations ✅
- [ ] Stable **Artifact ID** + **Version**
- [ ] **Who/what created it** (human/agent/CI) + timestamp
- [ ] **Inputs listed** with locations + checksums/digests
- [ ] **Processing steps** (tools, configs, params, code refs)
- [ ] **Outputs listed** with checksums/digests
- [ ] **License + restrictions** captured (including downstream constraints)
- [ ] **Sensitivity / CARE labels** captured (and inherited where applicable)
- [ ] **STAC + DCAT + PROV linkages** present (or explicitly N/A)
- [ ] **Validation results** recorded (schema + QA)
- [ ] **Review + approval** recorded

### Additional for narrative / AI outputs ✅
- [ ] Claims have **evidence citations** (or clearly labeled uncertainty)
- [ ] AI involvement disclosed (model, prompts, retrieved context)
- [ ] Governance ledger / audit reference included (if applicable)

### Additional for registry/supply-chain ✅
- [ ] OCI reference (name + digest)
- [ ] Signature reference (cosign)
- [ ] Attestation reference (in-toto/SLSA provenance) and/or PROV JSON-LD attachment

---

## 1) Attestation Summary 🧾

| Field | Value |
|---|---|
| **Attestation ID** | `{{ATTESTATION_ID}}` |
| **Status** | `draft` / `review` / `approved` / `superseded` |
| **Created At** | `{{ISO_8601_TIMESTAMP}}` |
| **Created By** | `{{HUMAN_OR_AGENT_NAME}}` |
| **Creator Type** | `human` / `agent` / `ci` |
| **Scope (Primary)** | `{{ATTESTATION_TYPE}}` |
| **Artifact Kind** | `dataset` / `layer` / `story_node` / `pulse_thread` / `simulation` / `ai_answer` / `export` / `graph_update` |
| **Artifact ID** | `{{KFM_CANONICAL_ID}}` |
| **Artifact Version** | `{{SEMVER_OR_DATE_VERSION}}` |
| **Supersedes** | `{{PRIOR_ATTESTATION_ID_OR_NA}}` |
| **Related PR / Issue** | `{{GITHUB_PR_OR_ISSUE_LINK_OR_NA}}` |
| **Run ID (if pipeline)** | `{{RUN_ID_OR_NA}}` |

> 🧠 **One-liner:**  
> `{{WHAT_THIS_ATTESTATION_ASSERTS_IN_ONE_SENTENCE}}`

---

## 2) Artifact Identity 🏷️

### 2.1 Canonical Identity (Required ✅)
- **Canonical ID:** `{{KFM_CANONICAL_ID}}`  
  - Example pattern: `kfm.<domain>.<artifact>.<variant>`  
- **Versioning scheme:** `{{SEMVER|DATE|CONTENT_HASH}}`
- **Artifact category:** `{{dataset|layer|story|model|graph|export}}`
- **Owner / Steward:** `{{TEAM_OR_PERSON}}`
- **Lifecycle:** `experimental` / `draft` / `published` / `deprecated`

### 2.2 Spatial + Temporal Extent (if applicable 🗺️⏳)
- **CRS / EPSG:** `{{EPSG_CODE_OR_WKT}}`
- **Spatial bbox:** `{{MINX,MINY,MAXX,MAXY}}`
- **Temporal interval:** `{{START_DATE}} → {{END_DATE}}`
- **Resolution / Scale:** `{{RESOLUTION_OR_SCALE}}`

### 2.3 Format + Storage (Required ✅)
- **Primary format(s):** `{{COG|GeoParquet|PMTiles|GeoJSON|CSV|JSON|PDF|PNG|glTF|3D Tiles|…}}`
- **Primary location:** `{{REPO_PATH_OR_OBJECT_URL}}`
- **Immutable digest(s):**  
  - `sha256:{{DIGEST}}`  
  - `multihash:{{OPTIONAL}}`

---

## 3) Evidence & Inputs 📚🔍

> **Evidence-first stack:** Inputs must be explicit, attributable, licensed, and hash-verifiable.

### 3.1 Evidence Triplet Links (STAC + DCAT + PROV) ✅

| Profile | Link / ID | Notes |
|---|---|---|
| **STAC Item/Collection** | `{{STAC_REF_OR_PATH}}` | Include bbox/time/source fields |
| **DCAT Dataset/Distribution** | `{{DCAT_REF_OR_PATH}}` | License + access + distributions |
| **PROV (JSON-LD preferred)** | `{{PROV_REF_OR_PATH}}` | Activities + entities + agents |

> If any are N/A, explain: `{{WHY_NA}}`

### 3.2 Source Inputs Table ✅

| Input ID | Type | Location | Checksum/Digest | License | Classification | Notes |
|---|---|---|---|---|---|---|
| `{{IN_001}}` | `raw_file|api_snapshot|dataset|document|model|code` | `{{PATH_OR_URL}}` | `sha256:{{...}}` | `{{SPDX_OR_TEXT}}` | `{{OPEN|RESTRICTED|CONFIDENTIAL|CULTURALLY_SENSITIVE}}` | `{{...}}` |
| `{{IN_002}}` |  |  |  |  |  |  |

### 3.3 Raw Intake Manifest (Required for ingestion ✅)
Attach or link:
- `📄 source.json` → `{{PATH_OR_LINK}}`
- `🔐 checksums.sha256` → `{{PATH_OR_LINK}}`
- `🧾 intake_notes.md` (optional) → `{{PATH_OR_LINK}}`

> 🧊 **Immutability rule:** Raw inputs should remain “as received.” Any corrections happen in derived layers with explicit transforms.

---

## 4) Processing & Methods 🛠️🧪

### 4.1 Pipeline / Activity Overview ✅
- **Activity name:** `{{PIPELINE_NAME}}`
- **Activity version:** `{{PIPELINE_VERSION}}`
- **Entry point:** `{{CLI_OR_SCRIPT}}`
- **Config file(s):** `{{CONFIG_PATHS}}`
- **Determinism claim:** `{{DETERMINISTIC_YES_NO}}`  
  - If yes, specify: seed(s), fixed clock, stable sort rules, pinned deps.
- **Run window:** `{{START_TS}} → {{END_TS}}`

### 4.2 Execution Context (Reproducibility) ✅
- **Git commit:** `{{GIT_SHA}}`
- **Repo URL:** `{{REPO_URL_OR_NA}}`
- **Container image:** `{{IMAGE_REF_OR_DIGEST}}`
- **Runtime:** `{{PYTHON|NODE|RUST|GO|JAVA}} {{VERSION}}`
- **OS/Arch:** `{{OS}} / {{ARCH}}`
- **Hardware (if relevant):** `{{CPU/GPU/RAM}}`

### 4.3 Step-by-step Activity Log ✅

| Step | Description | Tooling | Inputs | Outputs | Params/Notes |
|---:|---|---|---|---|---|
| 1 | `{{FETCH/SCRAPE/EXPORT}}` | `{{TOOL}}` | `{{IN_*}}` | `{{WORK_*}}` | `{{RATE_LIMITS|AUTH|SNAPSHOT_TS}}` |
| 2 | `{{CLEAN/NORMALIZE}}` | `{{TOOL}}` |  |  | `{{RULES}}` |
| 3 | `{{GEOREF/REPROJECT}}` | `{{GDAL/PROJ}}` |  |  | `{{TARGET_CRS|RESAMPLING}}` |
| 4 | `{{TILE/INDEX}}` | `{{TIPPECANOE|PMTILES|COG}}` |  |  | `{{TILING_SCHEME}}` |
| 5 | `{{PUBLISH_METADATA}}` | `{{STAC/DCAT/PROV}}` |  |  | `{{LINKING_RULES}}` |

> 🔁 If this is a **streaming** or **periodic refresh** pipeline, add cadence + snapshot boundary rules:
- **Cadence:** `{{HOURLY|DAILY|WEEKLY|EVENT_DRIVEN}}`
- **Snapshot boundary:** `{{“as-of” timestamp rule}}`
- **Idempotency key:** `{{KEY_OR_HASH}}`

### 4.4 Methodology (Optional but recommended 🧠)
Describe core algorithms/assumptions:
- `{{STATISTICAL_METHODS}}` (e.g., Bayesian model, regression, clustering)
- `{{GEO_METHODS}}` (e.g., kriging, resampling, interpolation)
- `{{GRAPH_METHODS}}` (e.g., centrality, community detection)
- `{{CV/NLP_METHODS}}` (e.g., OCR model, NER model)

---

## 5) Outputs & Distribution 📦🚀

### 5.1 Outputs Table ✅

| Output ID | Type | Location | Checksum/Digest | Format | Notes |
|---|---|---|---|---|---|
| `{{OUT_001}}` | `dataset|layer|tileset|report|graph_patch` | `{{PATH_OR_URL}}` | `sha256:{{...}}` | `{{COG|PMTiles|GeoParquet|…}}` | `{{...}}` |
| `{{OUT_002}}` |  |  |  |  |  |

### 5.2 UI / Layer Publishing (if applicable 🗺️)
- **Layer ID in UI:** `{{LAYER_ID}}`
- **Layer visibility rules:** `{{PUBLIC|LOGIN|ROLE_GATED}}`
- **Layer provenance panel link:** `{{UI_LINK_OR_NA}}`
- **Export attribution behavior:** `{{AUTO_CREDITS_ENABLED_YES_NO}}`

### 5.3 Knowledge Graph / DB Mutations (if applicable 🕸️🗄️)
- **DB target:** `PostGIS|Neo4j|Other`
- **Migration / import ID:** `{{MIGRATION_ID_OR_RUN_ID}}`
- **Tables/labels touched:** `{{LIST}}`
- **Row/node/edge counts:** `{{COUNTS}}`
- **Rollback strategy:** `{{PATCH|MIGRATION_DOWN|SNAPSHOT_RESTORE|N/A}}`

### 5.4 OCI Registry Publish (if applicable 🧊📦)
> Use when distributing big/binary artifacts (COGs, PMTiles, GeoParquet, glTF, reports) via content-addressable OCI.

- **OCI ref:** `{{REGISTRY}}/{{NAMESPACE}}/{{ARTIFACT}}:{{TAG}}`
- **OCI digest:** `sha256:{{DIGEST}}`
- **Registry visibility:** `public|private|restricted`
- **Attached referrers:**  
  - [ ] PROV JSON-LD  
  - [ ] SBOM  
  - [ ] in-toto/SLSA provenance  
  - [ ] Additional metadata bundle

---

## 6) Validation & QA ✅🧹

### 6.1 Schema + Metadata Validation ✅
- [ ] STAC schema validated (`{{TOOL}}`, `{{RESULT}}`)
- [ ] DCAT validated (`{{TOOL}}`, `{{RESULT}}`)
- [ ] PROV validated (`{{TOOL}}`, `{{RESULT}}`)
- [ ] Checksums verified end-to-end (`{{RESULT}}`)
- [ ] Data contract fields complete (source/license/extent/processing) (`{{RESULT}}`)

### 6.2 Data Quality Checks (Recommended ✅)
| Check | Result | Notes |
|---|---|---|
| Null rate / missingness | `{{PASS|WARN|FAIL}}` | `{{...}}` |
| Duplicate detection | `{{PASS|WARN|FAIL}}` | `{{...}}` |
| Outlier rules | `{{PASS|WARN|FAIL}}` | `{{...}}` |
| Spatial validity | `{{PASS|WARN|FAIL}}` | `{{...}}` |
| Temporal consistency | `{{PASS|WARN|FAIL}}` | `{{...}}` |

### 6.3 Bias / Drift (If AI/ML or human-impacting decisions ⚖️)
- **Bias checks performed:** `{{YES/NO}}`
- **Drift monitoring plan:** `{{YES/NO}}`
- **Known limitations:** `{{...}}`

---

## 7) AI / Automation Disclosure 🤖🧠

> This section is **Required ✅** if any AI agent, LLM, OCR model, classifier, or automated reasoning influenced the artifact.

### 7.1 AI Usage Summary ✅
- **AI used?** `YES/NO`
- **Where used:** `{{OCR|NER|summarization|classification|ranking|recommendation|generation}}`
- **Human in the loop?** `YES/NO`
- **How uncertainty is handled:** `{{CITATIONS|CONFIDENCE|REFUSAL_POLICY}}`

### 7.2 LLM / Agent Details (if applicable)
- **Model/provider:** `{{MODEL_NAME}}` (version `{{MODEL_VERSION_OR_DATE}}`)
- **Prompt / system strategy ID:** `{{PROMPT_PROFILE_ID}}`
- **Context bundle ID:** `{{CONTEXT_BUNDLE_ID}}`
- **Retrieval sources:** `{{LIST_DATASETS/LAYERS/DOCS}}`
- **Citations coverage:** `{{%_CITED}}`
- **Governance ledger entry:** `{{LEDGER_EVENT_ID_OR_LINK}}`

### 7.3 “Evidence-backed Output” Checklist ✅
- [ ] Claims are traceable to explicit sources
- [ ] Generated text is labeled (if presented to end users)
- [ ] Sensitive details filtered/redacted
- [ ] Any “best guess” is marked as such

---

## 8) Governance & Sensitivity ⚖️🔒

### 8.1 Classification & Access ✅
- **Classification:** `OPEN|INTERNAL|RESTRICTED|CONFIDENTIAL|CULTURALLY_SENSITIVE`
- **Reason:** `{{WHY}}`
- **Access control:** `public|role-gated|approval-required|never-export`
- **Downstream constraints inherit?** `YES/NO`  
  - If no, explain: `{{WHY_NOT}}`

### 8.2 FAIR + CARE (Recommended ✅)
- **FAIR notes:** `{{FINDABLE|ACCESSIBLE|INTEROPERABLE|REUSABLE}}`
- **CARE notes:** `{{COLLECTIVE_BENEFIT|AUTHORITY_TO_CONTROL|RESPONSIBILITY|ETHICS}}`

### 8.3 Privacy / Inference Control (If relevant 🧑‍⚖️)
- **PII present?** `YES/NO/UNKNOWN`
- **Aggregation level:** `{{POINT|HEX|COUNTY|STATE|ANONYMIZED}}`
- **Controls used (optional):**  
  - [ ] k-anonymity  
  - [ ] l-diversity  
  - [ ] t-closeness  
  - [ ] differential privacy (`ε={{EPSILON}}`, `δ={{DELTA}}`)  
  - [ ] query auditing / inference control  
- **Redaction strategy:** `{{...}}`

---

## 9) Security & Supply Chain 🔐🧯

### 9.1 Build Integrity ✅
- **SBOM available?** `YES/NO` → `{{SBOM_REF}}`
- **Pinned dependencies?** `YES/NO` → `{{LOCKFILES}}`
- **CI checks run?** `YES/NO` → `{{CI_RUN_LINK}}`

### 9.2 Attestations & Signatures (If distributed)
- **Cosign signature:** `{{COSIGN_REF_OR_LOG_INDEX}}`
- **SLSA/in-toto provenance:** `{{IN_TOTO_REF}}`
- **PROV JSON-LD attachment (if OCI):** `{{PROV_ATTACHMENT_REF}}`

---

## 10) Sign-off ✅✍️

| Role | Name | Identifier | Date | Signature/Approval |
|---|---|---|---|---|
| Prepared by | `{{NAME}}` | `{{ORCID|GITHUB|EMAIL}}` | `{{DATE}}` | `{{SIGNATURE_OR_NA}}` |
| Reviewed by | `{{NAME}}` | `{{...}}` | `{{DATE}}` | `{{APPROVED|CHANGES_REQUESTED}}` |
| Approved by | `{{NAME}}` | `{{...}}` | `{{DATE}}` | `{{APPROVED|N/A}}` |

> 🧩 Notes / review discussion:
- `{{LINK_TO_PULSE_THREAD_OR_PR_COMMENTS}}`

---

# Appendix A) Folder Conventions 📁🗺️

> Adapt if your repo layout differs, but keep the provenance chain explicit.

```text
📁 data/
  📁 raw/                  # ❄️ immutable “as received”
    📄 source.json
    🔐 checksums.sha256
  📁 work/                 # 🛠️ intermediate artifacts
  📁 processed/            # ✅ curated outputs
  📁 stac/                 # 🗺️ STAC collections/items
  📁 catalog/              # 🧭 DCAT dataset/distributions
  📁 prov/                 # ⛓️ PROV JSON-LD + attestations
  📁 audits/               # 🧾 NDJSON logs, run manifests, compliance evidence
```

---

# Appendix B) Machine-Readable Payloads 🤖📜

## B.1 PROV JSON-LD Skeleton (Recommended)
```json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "entity": {
    "{{OUT_001}}": {
      "prov:label": "{{HUMAN_READABLE_NAME}}",
      "prov:type": "{{dataset|layer|report|tileset}}",
      "kfm:artifact_id": "{{KFM_CANONICAL_ID}}",
      "kfm:version": "{{SEMVER_OR_DATE}}",
      "kfm:digest": "sha256:{{DIGEST}}",
      "kfm:classification": "{{CLASSIFICATION}}"
    }
  },
  "activity": {
    "{{RUN_ID}}": {
      "prov:label": "{{PIPELINE_NAME}}",
      "prov:startedAtTime": "{{START_TS}}",
      "prov:endedAtTime": "{{END_TS}}",
      "kfm:pipeline_version": "{{PIPELINE_VERSION}}",
      "kfm:git_commit": "{{GIT_SHA}}",
      "kfm:container_image": "{{IMAGE_DIGEST}}",
      "kfm:deterministic": "{{YES_NO}}",
      "kfm:seed": "{{SEED_OR_NA}}"
    }
  },
  "agent": {
    "{{CREATOR_ID}}": {
      "prov:label": "{{CREATOR_NAME}}",
      "prov:type": "{{human|agent|ci}}"
    }
  }
}
```

## B.2 SLSA / in-toto Provenance (Optional)
```json
{
  "_type": "https://in-toto.io/Statement/v1",
  "subject": [
    { "name": "{{OUT_001_LOCATION}}", "digest": { "sha256": "{{OUT_001_SHA256}}" } }
  ],
  "predicateType": "https://slsa.dev/provenance/v1",
  "predicate": {
    "buildDefinition": {
      "buildType": "{{PIPELINE_NAME}}@{{PIPELINE_VERSION}}",
      "externalParameters": {{ "config": "{{CONFIG_PATHS}}" }},
      "internalParameters": {{ "seed": "{{SEED_OR_NA}}" }},
      "resolvedDependencies": [
        { "uri": "{{IN_001_LOCATION}}", "digest": { "sha256": "{{IN_001_SHA256}}" } }
      ]
    },
    "runDetails": {
      "builder": { "id": "{{CI_OR_RUNNER_ID}}" },
      "metadata": { "invocationId": "{{RUN_ID}}" }
    }
  }
}
```

## B.3 Run Manifest (Idempotency / Canonicalization) ✅
> Store a stable `run_manifest.json`, canonicalize (e.g., RFC 8785), hash it, and link it here.

```json
{
  "run_id": "{{RUN_ID}}",
  "idempotency_key": "{{CANONICAL_SHA256}}",
  "pipeline": { "name": "{{PIPELINE_NAME}}", "version": "{{PIPELINE_VERSION}}" },
  "code": { "git_commit": "{{GIT_SHA}}", "repo": "{{REPO_URL}}" },
  "inputs": [{ "id": "{{IN_001}}", "sha256": "{{IN_001_SHA256}}" }],
  "outputs": [{ "id": "{{OUT_001}}", "sha256": "{{OUT_001_SHA256}}" }],
  "time": { "started": "{{START_TS}}", "ended": "{{END_TS}}" }
}
```

---

# Appendix C) Evidence Manifest (For Stories / Claims) 🗞️🧠

> If this attestation covers narrative claims (Story Node, AI Answer, report),
> include an evidence manifest so reviewers can audit each claim → sources.

```yaml
claims:
  - id: C001
    claim: "{{CLAIM_TEXT}}"
    confidence: "{{high|medium|low}}"
    citations:
      - source_id: "{{IN_001}}"
        locator: "{{page|line|timestamp|feature_id}}"
        note: "{{WHY_THIS_SUPPORTS_THE_CLAIM}}"
  - id: C002
    claim: "{{CLAIM_TEXT}}"
    confidence: "{{...}}"
    citations: []
    note: "No direct evidence found. Marked as hypothesis."
```

---

## ✅ Final “No Mystery” Self-Check
- [ ] Could a reviewer trace every output back to inputs + transforms?
- [ ] Are STAC/DCAT/PROV references present and consistent?
- [ ] Would you feel safe shipping this artifact to a public audience?
- [ ] If AI helped, is the involvement transparent and audit-ready?

> 🌾 KFM mantra: **“Trust is built from traceability.”**
