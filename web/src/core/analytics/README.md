# 📊 `core/analytics` — Privacy‑First Telemetry + Audit Signals (Web)

![TypeScript](https://img.shields.io/badge/TypeScript-Strict%20Types-informational)
![Frontend](https://img.shields.io/badge/Web-React%20%2B%20SPA-blue)
![Mapping](https://img.shields.io/badge/Maps-Geospatial%20UI-success)
![Principle](https://img.shields.io/badge/Principle-Provenance--First%20🧾-important)
![Principle](https://img.shields.io/badge/Principle-Privacy--First%20🛡️-critical)

> **What this module is:** a **thin, typed, dependency‑light** analytics core for the KFM web app that captures **usage telemetry**, **performance metrics**, and **audit‑grade signals** (e.g., redaction notices, provenance panel opens) without turning the project into a surveillance system.

---

## 🧭 Why `core/analytics` exists

KFM is built around **transparency**, **traceability**, and **evidence‑backed UX**. In practice, that means we need analytics that:

- ✅ Helps us learn what’s working (flows, features, performance)
- ✅ Supports governance (audit signals like “redaction notice shown”)
- ✅ Preserves trust (data minimization, consent gating, no PII by default)
- ✅ Stays debuggable (deterministic schema, typed events, predictable sinks)

**Analytics is a tool for improvement and accountability — not tracking.**

---

## 📦 What lives here (scope)

This folder should remain **framework‑agnostic** and **UI‑library‑agnostic** (no React imports). UI code calls into this module.

Typical contents (illustrative):

```text
📁 web/
  📁 src/
    📁 core/
      📁 analytics/
        📄 README.md ✅ (you are here)
        📄 index.ts
        📄 client.ts            # AnalyticsClient interface + default impl
        📄 events.ts            # Event taxonomy + types
        📄 context.ts           # Context enrichment (route/map/session)
        📄 redact.ts            # Privacy filters + sensitivity policy
        📄 queue.ts             # Buffering + batching + backpressure
        📁 sinks/
          📄 consoleSink.ts
          📄 memorySink.ts
          📄 httpSink.ts        # optional (adapter)
        📁 __tests__/
          📄 redact.test.ts
          📄 events.test.ts
```

> If the real folder structure differs, keep the **conceptual separation** even if filenames change.

---

## ✅ Core design principles

### 1) 🧾 Provenance‑aware by default
Events should carry *enough context* to connect UX behavior to:
- map state (zoom/bounds/layers),
- datasets & layer identifiers,
- “evidence surfaces” (citations/provenance panel interactions),
- AI advisory usage (Focus Mode events + redaction notices).

### 2) 🛡️ Privacy‑first (minimize + redact + consent)
- No raw PII (names, emails, exact addresses, free‑text) unless explicitly approved.
- Avoid storing **exact** geometry selections from users; prefer **binned/rounded** or **aggregate** representations.
- All sinks must be able to run in **“off / local only / remote”** modes.

### 3) 🧪 Measurement discipline (not vibes)
When analytics informs decisions:
- use experiments with proper design (randomization, guardrails, minimal measurable outcomes),
- analyze with regression/Bayesian methods when appropriate,
- and keep decisions reproducible.

### 4) ⚡ Low overhead + resilient
- Debounce high‑frequency streams (map move, hover).
- Backpressure & sampling are features, not failures.
- Must survive offline mode (queue locally, flush later if allowed).

---

## 🏗️ Architecture (port + adapters)

We treat analytics as a **core port** with pluggable **adapters/sinks**.

```mermaid
flowchart LR
  UI[🧩 UI Components] -->|track()| AC[📦 AnalyticsClient]
  AC --> ENR[🧠 Context Enricher]
  ENR --> POL[🛡️ Redaction + Sensitivity Policy]
  POL --> SMP[🎯 Sampling + Rate Limits]
  SMP --> Q[📬 Queue / Batch]
  Q --> CS[🖥️ Console Sink]
  Q --> MS[🧪 Memory Sink (tests)]
  Q --> HS[🌐 HTTP Sink (optional)]
```

**Rule:** `core/analytics` defines **interfaces + policy + data contracts**, while sinks handle IO.

---

## 🚀 Quickstart (developer ergonomics)

### Track a simple event
```ts
import { analytics } from "@/core/analytics"; // adjust alias to your project

analytics.track("ui_button_clicked", {
  component: "LayerToggle",
  action: "toggle",
  layer_id: "kfm.layer.railroads_1870",
});
```

### Track an audit‑signal event (Focus Mode)
```ts
analytics.track("focus_mode_redaction_notice_shown", {
  reason: "sensitive_source",
  redaction_level: "high",
  surface: "ai_answer_panel",
});
```

### Flush (only if your sink requires it)
```ts
await analytics.flush();
```

---

## 🧩 Event model

### Event name conventions 🏷️
Pick one convention and stick to it. KFM’s existing docs use snake_case examples, so we default to:

- ✅ `snake_case` with clear prefixes:
  - `ui_*`, `map_*`, `layer_*`, `search_*`, `ai_*`, `focus_mode_*`, `perf_*`, `error_*`, `audit_*`
- ❌ Avoid overly generic names like `click` or `open`.

### Event envelope (recommended)
```ts
export type AnalyticsEventName =
  | "ui_button_clicked"
  | "map_view_changed"
  | "layer_toggled"
  | "search_submitted"
  | "citation_panel_opened"
  | "focus_mode_redaction_notice_shown"
  | "perf_web_vitals"
  | "error_unhandled_exception"
  | "audit_export_started"
  // …extend intentionally (PR + review)

export type Sensitivity = "public" | "internal" | "restricted";

export interface AnalyticsEnvelope<TName extends string, TPayload extends object> {
  // identity
  name: TName;
  ts: string;              // ISO-8601
  schema_version: string;  // e.g. "1.0.0"

  // session + correlation
  session_id: string;      // random UUID (client generated)
  correlation_id?: string; // join events across flows

  // app context
  app: {
    env: "dev" | "staging" | "prod";
    build?: string;        // commit/sha/build id
    version?: string;      // semver
  };

  // privacy / governance
  sensitivity: Sensitivity;
  consent: {
    analytics: boolean;
    performance: boolean;
  };

  // optional: provenance surfaces
  provenance?: {
    dataset_ids?: string[];
    layer_ids?: string[];
    citation_ids?: string[];
  };

  // payload
  payload: TPayload;
}
```

> **Note:** Keep `payload` small. If it’s “big data”, it’s probably the wrong place.

---

## 🗺️ KFM‑specific context helpers (recommended)

Because KFM is a mapping + evidence platform, many useful events need **map context**:

- `map.zoom`
- `map.bounds` (rounded)
- `map.center` (rounded)
- `layers.visible` (IDs only)
- `timeline.range` (start/end)

Example context fragment:
```ts
export interface MapContext {
  zoom?: number; // integer or 0.5 increments
  center?: { lat: number; lng: number }; // rounded to ~3-4 decimals
  bounds?: { n: number; s: number; e: number; w: number }; // rounded
  visible_layer_ids?: string[];
}
```

✅ **Round** coordinates.  
❌ Don’t capture raw drawn polygons or precise user location unless the user explicitly opts in and we have a documented reason.

---

## 🧾 Audit‑grade events (minimum set)

These are “governance signals” we want to be able to prove happened:

- `focus_mode_redaction_notice_shown`
- `citation_panel_opened`
- `citation_clicked`
- `audit_export_started`
- `audit_export_completed`
- `audit_data_sensitivity_applied`
- `audit_terms_acknowledged` (if applicable)
- `audit_error_boundary_shown`

> These should be emitted even when “product analytics” is off **if** the user opted into governance logging — or be stored locally for the user (depending on policy). Keep policy explicit.

---

## 🛡️ Privacy, redaction, and sensitivity

### Recommended policy layers
1) **Field allow‑list** per event (schema first)
2) **PII scrubber** (defense in depth)
3) **Sensitivity classifier** (sets `sensitivity`)
4) **Consent gate** (drop or local‑only)
5) **Sampling** (especially for high‑volume events)

### Practical “do / don’t”
✅ DO:
- store **event counts**, **durations**, **binned values**
- store dataset/layer identifiers (non‑PII)
- store errors with **sanitized stack traces** (remove URLs/tokens)

❌ DON’T:
- store free‑text search queries verbatim (hash or categorize)
- store secrets, tokens, auth headers, URLs with query params
- store full geometry selections

---

## ⚡ Performance & batching guidelines

### High‑frequency events (debounce)
Events like `map_view_changed` can fire dozens of times per second. Use:
- debounce (e.g., 250–500ms)
- “last value wins” semantics in the queue
- sample (e.g., 10%)

### Queue rules of thumb
- cap queue size (prevent memory leaks)
- drop oldest low‑priority events first
- flush on:
  - tab hidden / beforeunload (best effort)
  - idle callbacks (when available)
  - time interval (e.g., 10–30s)

---

## 🧪 Testing strategy

Add a `memorySink` and assert:

- redaction removes forbidden keys
- envelope shape is stable (snapshot)
- schema_version increments intentionally
- sampling is deterministic under seeded RNG (if used)

Example:
```ts
import { createMemorySink } from "@/core/analytics/sinks/memorySink";

const sink = createMemorySink();
const analytics = createAnalyticsClient({ sinks: [sink], env: "test" });

analytics.track("ui_button_clicked", { component: "X", action: "Y" });

expect(sink.events[0].name).toBe("ui_button_clicked");
expect(sink.events[0].payload).toEqual({ component: "X", action: "Y" });
```

---

## 🔌 Adding a new sink (adapter)

Checklist:
- [ ] respects consent flags
- [ ] respects sensitivity policy (drops/aggregates restricted)
- [ ] handles backpressure (non‑blocking)
- [ ] fails “closed” (better to lose telemetry than crash UI)
- [ ] has test coverage

Minimal sink interface (example):
```ts
export interface AnalyticsSink {
  name: string;
  write(batch: Array<AnalyticsEnvelope<string, any>>): Promise<void> | void;
  flush?(): Promise<void> | void;
}
```

---

## 📈 Analysis workflows (how we use the data)

Analytics isn’t just collection — it’s interpretation.

Common workflows:
- **UX funnel analysis** (where users drop off)
- **Performance baselines** (tile loads, WebGL health, long tasks)
- **Experiment analysis** (A/B tests, feature flags)
- **Quality monitoring** (error rates by route/layer)

Recommended toolchain:
- Python notebooks for regression / causal-ish modeling
- Bayesian updates for “small data + uncertainty”
- R for fast EDA and visualization
- Postgres for storage + slicing (index wisely)

---

## 🧠 Cross‑discipline “why this design works” (project library)

<details>
<summary>📚 Stats + Experiments (decision quality)</summary>

- Regression modeling & reproducible experiments → **`regression-analysis-with-python.pdf`**, **`Regression analysis using Python - slides-linear-regression.pdf`**
- Hypothesis testing, experimental design, power, bias → **`Understanding Statistics & Experimental Design.pdf`**
- Bayesian reasoning under uncertainty → **`think-bayes-bayesian-statistics-in-python.pdf`**
- Practical EDA and visual checks → **`graphical-data-analysis-with-r.pdf`**

</details>

<details>
<summary>🗄️ Data management + performance (storage + scale)</summary>

- Query performance, indexing, throughput thinking → **`Database Performance at Scale.pdf`**
- Practical Postgres patterns → **`PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`**
- Scaling for future hardware + streaming ideas → **`Scalable Data Management for Future Hardware.pdf`**
- Data ecosystem framing → **`Data Spaces.pdf`**

</details>

<details>
<summary>🗺️ GIS, mapping, and spatial UX (context & map signals)</summary>

- Map design + cartographic clarity → **`making-maps-a-visual-guide-to-map-design-for-gis.pdf`**
- Mobile mapping considerations → **`Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`**
- Geospatial analysis + PostGIS workflows → **`python-geospatial-analysis-cookbook.pdf`**
- Remote sensing workflows → **`Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf`**
- 3D GIS considerations → **`Archaeological 3D GIS_26_01_12_17_53_09.pdf`**

</details>

<details>
<summary>🧱 Web UI + rendering (front-end constraints)</summary>

- Responsive UI constraints → **`responsive-web-design-with-html5-and-css3.pdf`**
- WebGL constraints + performance signals → **`webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`**
- Image formats + bandwidth tradeoffs → **`compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`**

</details>

<details>
<summary>🔐 Security + robustness (don’t leak, don’t break)</summary>

- Threat modeling mindset → **`ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`**
- Safe handling of low-level data + risk thinking → **`Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`**
- Concurrency patterns (queues, backpressure) → **`concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`**

</details>

<details>
<summary>🧠 Governance, ethics, and human-centered design</summary>

- Human-centered systems framing → **`Introduction to Digital Humanism.pdf`**
- AI era conceptual / legal framing → **`On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`**
- Autonomy & systems thinking (resilience patterns) → **`Principles of Biological Autonomy - book_9780262381833.pdf`**
- KFM system design context → **`Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`**, **`Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`**
- Repo-wide doc governance patterns → **`MARKDOWN_GUIDE_v13.md.gdoc`**, **`Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`**

</details>

<details>
<summary>📦 “Programming Books” compendiums (polyglot reference shelf)</summary>

These are project-wide reference compendiums used to support implementation details across languages and tooling:

- **`A programming Books.pdf`**
- **`B-C programming Books.pdf`**
- **`D-E programming Books.pdf`**
- **`F-H programming Books.pdf`**
- **`I-L programming Books.pdf`**
- **`M-N programming Books.pdf`**
- **`O-R programming Books.pdf`**
- **`S-T programming Books.pdf`**
- **`U-X programming Books.pdf`**

</details>

---

## 🧷 “Add a new event” checklist (PR template)

- [ ] Event name fits taxonomy (`ui_*`, `map_*`, `audit_*`, …)
- [ ] Added to `AnalyticsEventName` union (or registry)
- [ ] Payload is small, typed, and does not contain PII
- [ ] Sensitivity set correctly (`public` / `internal` / `restricted`)
- [ ] Emission is debounced if high-frequency
- [ ] Tests updated (shape + redaction)
- [ ] (If governance/audit) ensure event fires even when UI retries

---

## 🧯 Troubleshooting

- **No events?** Confirm consent gate and environment flags.
- **Too many events?** Add debounce/sampling at the producer or queue.
- **Payload rejected by backend?** Schema mismatch — bump `schema_version` and update the contract.
- **Performance regression?** Ensure map and hover events are not spamming; prefer aggregates.

---

## 📎 Appendix: Example event payloads

### `citation_panel_opened`
```json
{
  "name": "citation_panel_opened",
  "ts": "2026-01-15T12:34:56.789Z",
  "schema_version": "1.0.0",
  "session_id": "1f8c6f5c-2f0a-4f8a-8dc0-0c43a38d5c36",
  "app": { "env": "prod", "version": "0.1.0", "build": "abc123" },
  "sensitivity": "public",
  "consent": { "analytics": true, "performance": true },
  "provenance": { "citation_ids": ["cite:ks:atlas:1878:plate_4"] },
  "payload": {
    "surface": "right_sidebar",
    "entrypoint": "ai_answer_footer"
  }
}
```

### `map_view_changed` (debounced)
```json
{
  "name": "map_view_changed",
  "payload": {
    "zoom": 9,
    "center": { "lat": 38.50, "lng": -98.00 },
    "visible_layer_ids": ["kfm.layer.counties_1874", "kfm.layer.railroads_1870"]
  }
}
```

---

<!--
INTERNAL FILE CITATIONS (do not remove; helps provenance in this workspace)
:contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1} :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3} :contentReference[oaicite:4]{index=4} :contentReference[oaicite:5]{index=5} :contentReference[oaicite:6]{index=6}
:contentReference[oaicite:7]{index=7} :contentReference[oaicite:8]{index=8} :contentReference[oaicite:9]{index=9} :contentReference[oaicite:10]{index=10} :contentReference[oaicite:11]{index=11} :contentReference[oaicite:12]{index=12} :contentReference[oaicite:13]{index=13} :contentReference[oaicite:14]{index=14} :contentReference[oaicite:15]{index=15} :contentReference[oaicite:16]{index=16} :contentReference[oaicite:17]{index=17} :contentReference[oaicite:18]{index=18} :contentReference[oaicite:19]{index=19} :contentReference[oaicite:20]{index=20} :contentReference[oaicite:21]{index=21} :contentReference[oaicite:22]{index=22}
:contentReference[oaicite:23]{index=23} :contentReference[oaicite:24]{index=24} :contentReference[oaicite:25]{index=25} :contentReference[oaicite:26]{index=26} :contentReference[oaicite:27]{index=27} :contentReference[oaicite:28]{index=28} :contentReference[oaicite:29]{index=29} :contentReference[oaicite:30]{index=30} :contentReference[oaicite:31]{index=31} :contentReference[oaicite:32]{index=32} :contentReference[oaicite:33]{index=33} :contentReference[oaicite:34]{index=34} :contentReference[oaicite:35]{index=35} :contentReference[oaicite:36]{index=36} :contentReference[oaicite:37]{index=37}
:contentReference[oaicite:38]{index=38} :contentReference[oaicite:39]{index=39} :contentReference[oaicite:40]{index=40} :contentReference[oaicite:41]{index=41} :contentReference[oaicite:42]{index=42}
:contentReference[oaicite:43]{index=43} :contentReference[oaicite:44]{index=44} :contentReference[oaicite:45]{index=45} :contentReference[oaicite:46]{index=46} :contentReference[oaicite:47]{index=47} :contentReference[oaicite:48]{index=48} :contentReference[oaicite:49]{index=49} :contentReference[oaicite:50]{index=50} :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52} :contentReference[oaicite:53]{index=53} :contentReference[oaicite:54]{index=54} :contentReference[oaicite:55]{index=55} :contentReference[oaicite:56]{index=56} :contentReference[oaicite:57]{index=57}
:contentReference[oaicite:58]{index=58} :contentReference[oaicite:59]{index=59} :contentReference[oaicite:60]{index=60}
:contentReference[oaicite:61]{index=61} :contentReference[oaicite:62]{index=62} :contentReference[oaicite:63]{index=63} :contentReference[oaicite:64]{index=64} :contentReference[oaicite:65]{index=65} :contentReference[oaicite:66]{index=66} :contentReference[oaicite:67]{index=67} :contentReference[oaicite:68]{index=68} :contentReference[oaicite:69]{index=69} :contentReference[oaicite:70]{index=70} :contentReference[oaicite:71]{index=71} :contentReference[oaicite:72]{index=72} :contentReference[oaicite:73]{index=73} :contentReference[oaicite:74]{index=74} :contentReference[oaicite:75]{index=75}
:contentReference[oaicite:76]{index=76} :contentReference[oaicite:77]{index=77} :contentReference[oaicite:78]{index=78} :contentReference[oaicite:79]{index=79} :contentReference[oaicite:80]{index=80} :contentReference[oaicite:81]{index=81} :contentReference[oaicite:82]{index=82} :contentReference[oaicite:83]{index=83} :contentReference[oaicite:84]{index=84} :contentReference[oaicite:85]{index=85} :contentReference[oaicite:86]{index=86} :contentReference[oaicite:87]{index=87} :contentReference[oaicite:88]{index=88} :contentReference[oaicite:89]{index=89} :contentReference[oaicite:90]{index=90}
:contentReference[oaicite:91]{index=91} :contentReference[oaicite:92]{index=92} :contentReference[oaicite:93]{index=93} :contentReference[oaicite:94]{index=94} :contentReference[oaicite:95]{index=95} :contentReference[oaicite:96]{index=96} :contentReference[oaicite:97]{index=97} :contentReference[oaicite:98]{index=98} :contentReference[oaicite:99]{index=99} :contentReference[oaicite:100]{index=100} :contentReference[oaicite:101]{index=101} :contentReference[oaicite:102]{index=102} :contentReference[oaicite:103]{index=103} :contentReference[oaicite:104]{index=104} :contentReference[oaicite:105]{index=105}
:contentReference[oaicite:106]{index=106} :contentReference[oaicite:107]{index=107} :contentReference[oaicite:108]{index=108} :contentReference[oaicite:109]{index=109} :contentReference[oaicite:110]{index=110} :contentReference[oaicite:111]{index=111} :contentReference[oaicite:112]{index=112} :contentReference[oaicite:113]{index=113} :contentReference[oaicite:114]{index=114} :contentReference[oaicite:115]{index=115} :contentReference[oaicite:116]{index=116} :contentReference[oaicite:117]{index=117} :contentReference[oaicite:118]{index=118} :contentReference[oaicite:119]{index=119} :contentReference[oaicite:120]{index=120}
:contentReference[oaicite:121]{index=121} :contentReference[oaicite:122]{index=122} :contentReference[oaicite:123]{index=123} :contentReference[oaicite:124]{index=124} :contentReference[oaicite:125]{index=125} :contentReference[oaicite:126]{index=126} :contentReference[oaicite:127]{index=127} :contentReference[oaicite:128]{index=128} :contentReference[oaicite:129]{index=129} :contentReference[oaicite:130]{index=130} :contentReference[oaicite:131]{index=131} :contentReference[oaicite:132]{index=132} :contentReference[oaicite:133]{index=133} :contentReference[oaicite:134]{index=134} :contentReference[oaicite:135]{index=135}
:contentReference[oaicite:136]{index=136} :contentReference[oaicite:137]{index=137} :contentReference[oaicite:138]{index=138} :contentReference[oaicite:139]{index=139} :contentReference[oaicite:140]{index=140} :contentReference[oaicite:141]{index=141} :contentReference[oaicite:142]{index=142} :contentReference[oaicite:143]{index=143} :contentReference[oaicite:144]{index=144} :contentReference[oaicite:145]{index=145} :contentReference[oaicite:146]{index=146} :contentReference[oaicite:147]{index=147} :contentReference[oaicite:148]{index=148} :contentReference[oaicite:149]{index=149} :contentReference[oaicite:150]{index=150}
:contentReference[oaicite:151]{index=151} :contentReference[oaicite:152]{index=152} :contentReference[oaicite:153]{index=153} :contentReference[oaicite:154]{index=154} :contentReference[oaicite:155]{index=155} :contentReference[oaicite:156]{index=156} :contentReference[oaicite:157]{index=157} :contentReference[oaicite:158]{index=158} :contentReference[oaicite:159]{index=159} :contentReference[oaicite:160]{index=160} :contentReference[oaicite:161]{index=161} :contentReference[oaicite:162]{index=162} :contentReference[oaicite:163]{index=163} :contentReference[oaicite:164]{index=164} :contentReference[oaicite:165]{index=165}
:contentReference[oaicite:166]{index=166} :contentReference[oaicite:167]{index=167} :contentReference[oaicite:168]{index=168} :contentReference[oaicite:169]{index=169} :contentReference[oaicite:170]{index=170} :contentReference[oaicite:171]{index=171} :contentReference[oaicite:172]{index=172} :contentReference[oaicite:173]{index=173} :contentReference[oaicite:174]{index=174} :contentReference[oaicite:175]{index=175} :contentReference[oaicite:176]{index=176} :contentReference[oaicite:177]{index=177} :contentReference[oaicite:178]{index=178} :contentReference[oaicite:179]{index=179} :contentReference[oaicite:180]{index=180}
:contentReference[oaicite:181]{index=181} :contentReference[oaicite:182]{index=182} :contentReference[oaicite:183]{index=183} :contentReference[oaicite:184]{index=184} :contentReference[oaicite:185]{index=185} :contentReference[oaicite:186]{index=186} :contentReference[oaicite:187]{index=187} :contentReference[oaicite:188]{index=188} :contentReference[oaicite:189]{index=189} :contentReference[oaicite:190]{index=190} :contentReference[oaicite:191]{index=191} :contentReference[oaicite:192]{index=192} :contentReference[oaicite:193]{index=193} :contentReference[oaicite:194]{index=194} :contentReference[oaicite:195]{index=195}
-->

