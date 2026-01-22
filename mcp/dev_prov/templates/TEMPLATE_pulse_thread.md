---
template:
  id: "TEMPLATE_pulse_thread"
  version: "1.0.0"
  intent: "Geotagged, time-scoped, evidence-backed update thread designed for KFM map pop-ups + side-panel feed."
  notes:
    - "Keep it short + high-signal. If it becomes a long narrative, promote to a Story Node."
    - "Evidence-first: factual claims should be traceable to the Evidence Manifest + citations."

kfm:
  content_type: "pulse_thread"
  schema_version: "kfm.pulse_thread.v1"
  id: "{{pulse_id}}"               # e.g., PT-2026-01-22-0001
  slug: "{{slug}}"                 # kebab-case
  title: "{{title}}"
  status: "draft"                  # draft|review|published|archived
  visibility: "internal"           # public|internal|restricted
  created_at: "{{created_at_iso}}"
  updated_at: "{{updated_at_iso}}"
  language: "en"
  region_slug: "{{region_slug}}"   # e.g., kansas
  owners:
    - "{{owner_handle}}"           # e.g., @maintainer
  contributors:
    - "{{contributor_handle}}"     # e.g., @domain-expert
  reviewers:
    - "{{reviewer_handle}}"        # optional; required if AI-assisted or sensitive

  ai_assistance:
    used: false
    disclosure_label: "none"       # none|assisted|drafted
    models: []                     # e.g., ["gpt-4.1", "local-rag-v2"]
    human_review_required: true
    governance_ledger_ref: "{{governance_ledger_ref}}"  # append-only log pointer, if available

time:
  as_of: "{{as_of_iso}}"           # when the data was retrieved / computed
  window:
    start: "{{window_start_iso}}"
    end: "{{window_end_iso}}"
  event_time:
    start: "{{event_start_iso}}"   # optional: when the real-world event began
    end: "{{event_end_iso}}"       # optional: when it ended / last observed
  cadence:
    expected_update: "{{cadence}}" # e.g., hourly|daily|weekly|ad-hoc

geo:
  bbox_wgs84: ["{{min_lon}}", "{{min_lat}}", "{{max_lon}}", "{{max_lat}}"]
  centroid_wgs84: ["{{centroid_lon}}", "{{centroid_lat}}"]
  geometry_geojson:
    enabled: false
    feature_collection: null       # optional; set enabled:true and include GeoJSON FeatureCollection
  places:
    - graph_id: "{{place_graph_id}}"   # e.g., neo4j://Place/123
      label: "{{place_label}}"         # e.g., "Kansas River — Topeka gauge"
      kind: "Place|Region|County|Watershed|HUC8|HUC12|Station|TribalLand"
  precision:
    level: "exact"                 # exact|generalized
    generalization_method: ""      # e.g., h3_7|county|huc8|bbox|10km_rounding
    redaction_notes: ""            # why/what was generalized

themes:
  concepts:
    - graph_id: "{{concept_graph_id}}" # e.g., neo4j://Concept/drought
      label: "{{concept_label}}"       # e.g., "Drought"
  tags: ["{{tag1}}", "{{tag2}}", "{{tag3}}"]

signals:
  trigger:
    type: "manual"                 # anomaly|scheduled|manual|sensor_threshold|news|community_report
    watcher_id: "{{watcher_id}}"   # optional
    watcher_event_id: "{{watcher_event_id}}" # optional; stable event ref for provenance
  detection:
    detector: "human"              # EWMA|CUSUM|threshold|rule|human
    metric: "{{metric_name}}"      # e.g., river_stage_ft, pm25_ugm3, wildfire_hotspots
    baseline_window: "{{baseline_window}}" # e.g., 30d rolling
    current_window: "{{current_window}}"   # e.g., last 6h
    score: "{{score}}"             # optional numeric/string
    threshold: "{{threshold}}"     # optional numeric/string
    confidence: "medium"           # low|medium|high
    uncertainty_notes: ""

impact:
  severity: "medium"               # low|medium|high|critical
  affected_populations: ""         # optional; keep non-sensitive
  stakeholders:
    - "{{stakeholder1}}"
  potential_harms:
    - ""                           # list possible harms; helps CARE/ethics gating
  limitations:
    - ""                           # known caveats / missing data / uncertainties

evidence:
  required: true
  citations_in_text: true
  evidence_manifest_path: "{{evidence_manifest_path}}"  # e.g., ./evidence/EM-{{pulse_id}}.yaml
  prov_bundle_path: "{{prov_jsonld_path}}"              # e.g., ./prov/PT-{{pulse_id}}.jsonld

  catalogs:
    stac_items: ["{{stac_item_ref}}"]                   # file path or ID
    dcat_datasets: ["{{dcat_dataset_ref}}"]             # file path or ID

  queries:
    - name: "{{query_name}}"
      engine: "postgis|neo4j|sparql|duckdb|api"
      statement: "{{query_statement}}"
      parameters: {}
      result_artifact_ref: "{{result_artifact_ref}}"    # e.g., oci://registry/kfm/pulses/PT...:results
      result_digest_sha256: "{{result_sha256}}"

dev_prov:
  run:
    run_id: "{{run_id}}"
    run_manifest_path: "{{run_manifest_path}}"          # e.g., data/audits/<run_id>/run_manifest.json
    idempotency_key: "{{idempotency_key}}"
    canonical_digest: "{{canonical_digest}}"

  policy_gates:
    # Minimum v13-style gates (fail-closed) — mark pass/fail in CI or automation logs
    schema_validation: "unknown"         # pass|fail|unknown
    stac_dcat_prov_completeness: "unknown"
    license_presence: "unknown"
    sensitivity_classification: "unknown"
    provenance_completeness: "unknown"
    ai_citations_required: "unknown"

  security_attestations:
    sbom_ref: "{{sbom_ref}}"             # SPDX or similar
    slsa_attestation_ref: "{{slsa_ref}}" # in-toto/SLSA provenance statement
    sigstore_bundle_ref: "{{sigstore_bundle_ref}}"

ui:
  surfaces: ["map_popup", "side_panel_feed"]    # expected UI placements
  icon: "pulse"
  map_view:
    lon: "{{centroid_lon}}"
    lat: "{{centroid_lat}}"
    zoom: "{{zoom}}"
    pitch: "{{pitch}}"
    bearing: "{{bearing}}"
  suggested_layers_on:
    - "{{layer_id}}"
  callouts:
    highlight_features: []                      # optional feature IDs to highlight in UI

related:
  pulse_threads:
    - id: "{{related_pulse_id}}"
      relation: "followup"                      # followup|supersedes|duplicates|context
  story_nodes: ["{{story_node_id}}"]
  datasets: ["{{dataset_id}}"]
  issues: ["{{issue_id_or_url}}"]               # optional: maintainer issue for tracking

exports:
  federation_ready: false                       # true if safe to federate beyond region
  json_serialization_ref: "{{json_export_ref}}" # optional: where JSON export lives
---

# 🫀 Pulse Thread: {{title}}

![KFM](https://img.shields.io/badge/KFM-pulse_thread-blue) ![Status](https://img.shields.io/badge/status-draft-lightgrey) ![Evidence](https://img.shields.io/badge/evidence-required-green) ![Provenance](https://img.shields.io/badge/prov-linked-purple)

> [!NOTE]
> Pulse Threads are **geotagged “what’s happening” updates** that stay *tight, traceable, and updatable*. They can render as **map pop-ups** or a **side-panel feed** and should always point to an **Evidence Manifest** + **PROV bundle** for verification.

> [!TIP]
> If this thread becomes a stable, longer narrative (multi-step playback, heavy media, multiple map states), **promote it to a Story Node** and link back here under `related.story_nodes`.

---

## 📌 Quick Facts

| Field | Value |
|---|---|
| 🗺️ Area | {{place_label}} |
| 📍 Center | ({{centroid_lat}}, {{centroid_lon}}) |
| 🗓️ Window | {{window_start_iso}} → {{window_end_iso}} |
| ⏱️ As-of | {{as_of_iso}} |
| 🚦 Status | {{kfm.status}} |
| 🔥 Severity | {{impact.severity}} |
| 🎯 Confidence | {{signals.detection.confidence}} |
| 🧭 Trigger | {{signals.trigger.type}} / {{signals.detection.detector}} |
| 🔒 Visibility | {{kfm.visibility}} |

---

## 🧠 TL;DR (3–6 bullets)

- {{tldr_bullet_1}} [^1]
- {{tldr_bullet_2}} [^2]
- {{tldr_bullet_3}} [^3]

> [!IMPORTANT]
> Keep TL;DR factual. Put hypotheses in **Interpretation** and label them clearly.

---

## 🗺️ Map & Timeline Context

**Why this location?**  
{{why_location}}

**Why this time window?**  
{{why_time_window}}

**Suggested map layers to toggle on:**  
- `{{layer_id}}` — {{layer_reason}}
- `{{layer_id_2}}` — {{layer_reason_2}}

---

## 📈 Signal / What Changed

### Observations (facts only)
- {{observation_1}} [^1]
- {{observation_2}} [^2]

### Detector / Trigger Details
- **Detector:** `{{signals.detection.detector}}`
- **Metric:** `{{signals.detection.metric}}`
- **Baseline:** `{{signals.detection.baseline_window}}`
- **Current window:** `{{signals.detection.current_window}}`
- **Score / Threshold:** `{{signals.detection.score}} / {{signals.detection.threshold}}`

---

## 🧾 Evidence Snapshot

> [!NOTE]
> This section should be **enough to verify the punchline**, without scrolling forever. Put the *full inventory* in the Evidence Manifest at: `{{evidence_manifest_path}}`.

| Indicator | Baseline | Current | Delta | Source / Query | Confidence |
|---|---:|---:|---:|---|---|
| {{indicator_1}} | {{baseline_1}} | {{current_1}} | {{delta_1}} | [^1] | {{conf_1}} |
| {{indicator_2}} | {{baseline_2}} | {{current_2}} | {{delta_2}} | [^2] | {{conf_2}} |

### Key Evidence Notes
- {{evidence_note_1}} [^1]
- {{evidence_note_2}} [^2]

---

## 🧩 Interpretation (label assumptions + uncertainty)

> [!WARNING]
> Interpretation can be wrong. Keep it modular, explicit, and falsifiable.

- **Hypothesis A:** {{hypothesis_a}}  
  - **Supports:** {{supports_a}} [^1]  
  - **Could be falsified by:** {{falsify_a}}  
- **Hypothesis B:** {{hypothesis_b}}  
  - **Supports:** {{supports_b}} [^2]  
  - **Could be falsified by:** {{falsify_b}}  

---

## 🎯 Impact & Stakeholders

### What might be affected?
- {{impact_item_1}}
- {{impact_item_2}}

### Who should care / coordinate?
- {{stakeholder_1}}
- {{stakeholder_2}}

### Known limitations
- {{limitation_1}}
- {{limitation_2}}

---

## ✅ Recommended Actions (next 24–72h)

- [ ] **Verify**: {{verify_step_1}} (owner: {{owner_handle}}) [^1]  
- [ ] **Investigate**: {{investigate_step_1}} (owner: {{contributor_handle}}) [^2]  
- [ ] **Mitigate / Communicate**: {{mitigate_step_1}} (owner: {{stakeholder1}})  
- [ ] **Update this thread** with results + new citations (append-only mindset)

---

## 🔁 Updates & Change Log (append-only)

> [!TIP]
> Prefer adding a dated update over rewriting older claims. If you must correct, **strike-through** the old line and note why.

- **{{update_date_1}}** — {{update_summary_1}} [^4]
- **{{update_date_2}}** — {{update_summary_2}} [^5]

---

## 🔗 Related Graph Links

- **Related Pulse Threads:** {{related_pulse_id}} ({{relation_type}})
- **Related Story Nodes:** {{story_node_id}}
- **Datasets / Catalog IDs:** {{dataset_id}}
- **Issue / Tracking:** {{issue_id_or_url}}

---

## ⚖️ FAIR + CARE Checklist

> [!NOTE]
> This is a quick “go/no-go” scan before publishing widely or federating.

### FAIR
- [ ] **Findable**: IDs + tags + bbox/time filled
- [ ] **Accessible**: evidence links resolve (repo paths / API / registry refs)
- [ ] **Interoperable**: uses STAC/DCAT/PROV refs where applicable
- [ ] **Reusable**: license + provenance + methods/queries included

### CARE
- [ ] **Collective Benefit**: benefit/harms noted
- [ ] **Authority to Control**: respects cultural/community constraints
- [ ] **Responsibility**: sensitivity classification + redaction strategy applied
- [ ] **Ethics**: avoids exposing sensitive coordinates / PII

---

## ⛓️ Provenance & Artifacts

### “View Evidence” entrypoints
- **Evidence Manifest:** `{{evidence_manifest_path}}`
- **PROV bundle (JSON-LD):** `{{prov_jsonld_path}}`
- **Run manifest:** `{{run_manifest_path}}` (run_id: `{{run_id}}`)

### Dev/Automation lineage (W-P-E)
- **Watcher event:** `{{watcher_event_id}}`
- **Planner plan:** `{{planner_plan_id}}`
- **Executor job:** `{{executor_job_id}}`
- **Idempotency key:** `{{idempotency_key}}`
- **Canonical digest:** `{{canonical_digest}}`

---

## 🧷 Tiny Citation Block (3–7 lines)

> [!IMPORTANT]
> Keep this compact. The full inventory belongs in the Evidence Manifest.

[^1]: {{citation_1_short}}
[^2]: {{citation_2_short}}
[^3]: {{citation_3_short}}
[^4]: {{citation_4_short}}
[^5]: {{citation_5_short}}

---

## 🧪 Appendix: Queries (optional but recommended)

<details>
<summary><strong>🔎 Query 1 — {{query_name}}</strong></summary>

**Engine:** {{engine}}  
**Statement:**
```sql
{{query_statement}}
```

**Parameters:**
```json
{{query_parameters_json}}
```

**Result artifact ref:** `{{result_artifact_ref}}`  
**SHA-256:** `{{result_sha256}}`

</details>

---

## 📦 Appendix: Companion Files (recommended layout)

```text
📁 pulse_threads/
  📄 {{pulse_id}}.md
  📁 evidence/
    📄 EM-{{pulse_id}}.yaml
  📁 prov/
    📄 PT-{{pulse_id}}.jsonld
  📁 audits/
    📄 run_manifest_{{run_id}}.json
```

<details>
<summary><strong>🧾 Evidence Manifest stub (EM-{{pulse_id}}.yaml)</strong></summary>

```yaml
schema_version: "kfm.evidence_manifest.v1"
id: "EM-{{pulse_id}}"
for:
  content_type: "pulse_thread"
  content_id: "{{pulse_id}}"
as_of: "{{as_of_iso}}"

evidence:
  - id: "EV-001"
    kind: "dataset|document|api_call|analysis_output"
    title: "{{evidence_title}}"
    source_url: "{{source_url_or_path}}"
    license: "{{license}}"
    retrieved_at: "{{retrieved_at_iso}}"
    checksum_sha256: "{{sha256}}"
    used_for:
      - claim_ref: "[^1]"
        note: "{{how_used}}"

queries:
  - id: "Q-001"
    engine: "{{engine}}"
    statement: "{{query_statement}}"
    parameters: {}
    result_digest_sha256: "{{result_sha256}}"

transforms:
  - id: "T-001"
    description: "{{transform_description}}" # e.g., "monthly aggregation", "cropped AOI", "geo-generalized"
    inputs: ["EV-001"]
    outputs: ["EV-002"]
```

</details>

<details>
<summary><strong>⛓ PROV stub (PT-{{pulse_id}}.jsonld)</strong></summary>

```json
{
  "@context": [
    "https://www.w3.org/ns/prov.jsonld",
    { "kfm": "https://kansasfrontiermatrix.example/ns#" }
  ],
  "@graph": [
    {
      "@id": "kfm:pulse/{{pulse_id}}",
      "@type": ["kfm:PulseThread", "prov:Entity"],
      "prov:generatedAtTime": "{{created_at_iso}}",
      "prov:wasDerivedFrom": ["kfm:evidence/EM-{{pulse_id}}"]
    },
    {
      "@id": "kfm:activity/run/{{run_id}}",
      "@type": "prov:Activity",
      "prov:startedAtTime": "{{run_started_at}}",
      "prov:endedAtTime": "{{run_ended_at}}",
      "prov:used": ["kfm:evidence/EM-{{pulse_id}}"],
      "prov:generated": ["kfm:pulse/{{pulse_id}}"],
      "prov:wasAssociatedWith": "kfm:agent/{{owner_handle}}"
    }
  ]
}
```

</details>

---

<!--
Template provenance (human-readable):
- Evidence Manifest + tiny citation block + “View Evidence” UX patterns
- STAC/DCAT/PROV and provenance-first intake philosophy
- Automated policy gates + W-P-E automation + run_manifest hashing/idempotency
- UI surfaces (map pop-ups, side panels, provenance panels, focus mode explainability)
- FAIR+CARE governance + sensitivity-aware generalization + supply chain attestations
-->
