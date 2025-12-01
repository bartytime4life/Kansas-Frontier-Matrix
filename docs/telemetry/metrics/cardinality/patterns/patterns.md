<div align="center">

# 📊 **Metric Cardinality Patterns & Anti-Patterns — Detailed Examples**  
`docs/telemetry/metrics/cardinality/patterns/patterns.md`

**Purpose**  
Provide the **complete, example-rich expansion** of the governed patterns & anti-patterns defined in this directory’s README.  
This file supplies **explicit, concrete “good vs bad” examples** for engineering, CI validation, and Story Node generation.

</div>

---

## 🧱 Patterns (Approved)

### ✔ Pattern 1 — Use **Bounded Vocabularies**
Metric label values MUST come from a **finite**, **documented**, **stable** list.

**Correct**

~~~text
status="ok"
status="error"
layer="soil"
layer="precip"
~~~

**Why it matters**

- Prevents unbounded growth from free-text values  
- Enables deterministic aggregation  
- Simplifies Focus Mode entity linking  

---

### ✔ Pattern 2 — Apply **Binning** to Range-Like Dimensions
Zoom, elevation, resolution, and file size MUST be **bucketed**.

**Correct**

~~~text
zoom_bin="5-8"
elev_bin="200-400"
size_class="medium"
resolution="high"
~~~

**Incorrect**

~~~text
zoom="11"
elev="237"
filesize_bytes="4892334"
~~~

---

### ✔ Pattern 3 — Normalize Paths / URLs (Never Use Literal Values)
Paths belong in **logs** or **traces**, not labels.

**Correct**

~~~text
/api/user/:id/items/:id
/tiles/:z/:x/:y
~~~

**Incorrect**

~~~text
file_path="/home/worker/tmp/load/8138.tif"
http_url="/tiles/11/345/892"
~~~

---

### ✔ Pattern 4 — Encode **Categories**, Not **Instances**
Labels should reflect **types**, **modes**, or **buckets** — never specific objects.

**Correct**

~~~text
method="merge"
component="tiler"
dataset_release="v11.2"
phase="ingest"
~~~

**Incorrect**

~~~text
instance="tiler-95cd7f1c8f-zbg9x"
pod_id="tiler-8bcdf4"
host="node-14"
~~~

---

### ✔ Pattern 5 — Use **Enumerated Status Labels**
Status MUST be chosen from the predefined vocabulary.

Allowed values:

- `ok`
- `success`
- `error`
- `timeout`
- `retry`
- `skipped`

**Correct**

~~~text
status="ok"
status="timeout"
~~~

**Incorrect**

~~~text
status="weird-half-broken-state"
status="409"
~~~

---

## 📉 Anti-Patterns (Prohibited)

### ❌ Anti-Pattern 1 — Using Unique IDs as Labels
These destroy Active Series Budgets.

~~~text
trace_id="54bdfe1"
session_id="a8f1d19c"
feature_id="abc123"
user_id="991"
~~~

Governed Response:

- Immediate **quarantine**  
- **deny-match** for offending metric  
- **Story Node seed** created  
- Entry added to **review-log**  

---

### ❌ Anti-Pattern 2 — Coordinates or H3 Cells
Geospatial values cause unbounded series growth.

~~~text
lat="38.992"
lon="-95.226"
h3="8f28308280f1fff"
~~~

Correct placement:

- Traces → allowed  
- Logs → allowed  
- Metrics → **forbidden**  

---

### ❌ Anti-Pattern 3 — Raw Paths / URLs in Labels

~~~text
file_path="/opt/data/bigfile/2025/11/30/data.csv"
http_url="/tiles/13/2201/1511"
~~~

Use normalized placeholders instead.

---

### ❌ Anti-Pattern 4 — Free-Form Label Values

~~~text
why="sometimes it just crashes when the moon is out"
reason="missing metadata for collection but it works on my machine"
~~~

Any uncontrolled string is automatically a cardinality leak.

---

### ❌ Anti-Pattern 5 — Per-Entity Metric Naming

~~~text
kfm_graph_upserts_feature_abc123_total
kfm_tile_latency_13_2201_1511_seconds
~~~

Metrics must be **family-stable**, with differences expressed using **allowed labels** (bounded).

---

## 🧪 CI Enforcement Examples

### CI MUST FAIL the following samples:

~~~text
kfm_ingest_total{http_url="/tiles/11/345"}               # forbidden label
kfm_tile_build_seconds{stac_id="20251130T2100Z"}         # per-object ID
kfm_graph_upserts_total{feature_id="abc123"}             # unbounded value
kfm_ingest_total{lat="38.99", lon="-95.22"}              # coordinates
~~~

### CI MUST PASS the following samples:

~~~text
kfm_ingest_total{dataset="usgs_hydro", status="ok"}
kfm_tile_build_seconds{layer="soil", zoom_bin="9-12"}
kfm_graph_upserts_total{op="merge", dataset_release="v11.2"}
~~~

---

## 🧠 Story Node & Focus Mode Integration

Pattern and anti-pattern events generate narrative-grade material.

### When an anti-pattern appears:

- Create a **Story Node seed** describing the anomaly  
- Attach PROV-O lineage (activity → agent → entity)  
- Add an entry to `review-log.md`  
- Link the event to:
  - deployment commit  
  - service  
  - environment  

### Focus Mode MAY surface:

- “Spike Timeline”  
- “New Label Introduced”  
- “ASB Violation”  
- “Remediation Sequence”  

Patterns, meanwhile, act as **rulesets** Focus Mode uses for:

- Explaining why certain labels are allowed  
- Highlighting which labels are dangerous  
- Understanding how metrics relate to governance  

---

<div align="center">

📊 **KFM v11 — Metric Cardinality Patterns**  
Deterministic Metrics · Sustainable Telemetry · FAIR+CARE-Aligned  

[⬅ Back to patterns README](./README.md)

</div>

