# 🔒 Core Security — `web/src/core/security`

![Security](https://img.shields.io/badge/security-core-%F0%9F%94%92-blue)
![Defense in Depth](https://img.shields.io/badge/defense--in--depth-layered-success)
![Provenance First](https://img.shields.io/badge/provenance--first-%F0%9F%A7%BE-brightgreen)
![Policy](https://img.shields.io/badge/policy-no__mystery__layers-important)
![Privacy](https://img.shields.io/badge/privacy-redaction%20%26%20aggregation-critical)

> 📍 **Path:** `web/src/core/security/README.md`  
> 🧭 **Purpose:** a single, opinionated security hub for **client-side** safeguards, policy evaluation, redaction, and safe rendering — aligned with KFM’s governance + provenance model.

---

## 🧠 What this module is responsible for

This folder is the **security “front-door”** for the web client. It provides:

- **🪪 Auth context shaping** (turn token/user/org info into a single `SecurityContext`)
- **🧰 Authorization helpers** (client-side gating for UX + safety; server remains source-of-truth)
- **🏷️ Data classification & policy evaluation** (Public/Internal/Confidential/Restricted)
- **🧼 Safe rendering** (sanitized Markdown/HTML, safe external links, safe URL handling)
- **✂️ Redaction & generalization** for sensitive attributes / geospatial precision
- **🧾 Provenance hooks** (ensure UI/Focus Mode outputs remain traceable + citable)
- **🛰️ Audit/telemetry events** for security-relevant UI actions (redaction applied, blocked views, etc.)

KFM’s architecture explicitly treats the **front-end as untrusted** and relies on server-side validation and enforcement; the UI’s job is to be safe-by-default and prevent accidental leakage while still assuming the backend is the gatekeeper. :contentReference[oaicite:0]{index=0}

---

## 📌 Non‑goals (important)

- ❌ **This is not a substitute for backend enforcement.**  
  The API must validate input, enforce roles, and control sensitive data access. :contentReference[oaicite:1]{index=1}
- ❌ **No “security by obfuscation.”**  
  We reduce accidental exposure, but we assume attackers can read client code.
- ❌ **No “mystery layers.”**  
  If the UI can’t explain where a layer/fact came from, it doesn’t belong in official views. :contentReference[oaicite:2]{index=2}

---

## 🧱 Security invariants (these must always hold)

> [!IMPORTANT]
> These are **hard rules** for any code that touches user-visible content, exports, or AI responses.

1) **🔐 “No output less restricted than its input.”**  
   Downstream products (UI views, exports, Focus Mode answers) **must not weaken** the input classification — restrictions only stay the same or get tighter. :contentReference[oaicite:3]{index=3}

2) **✂️ Redaction applies everywhere (not just UI).**  
   Redaction/generalization should be enforced at each relevant layer (processed data, metadata, API, UI). :contentReference[oaicite:4]{index=4}

3) **🧾 Auditability is mandatory.**  
   Classification changes, sensitive views, and redaction behavior must leave audit/telemetry trails. :contentReference[oaicite:5]{index=5}

4) **🧬 Provenance-first UI.**  
   Anything shown in UI or Focus Mode should be traceable to cataloged sources + provable processing. :contentReference[oaicite:6]{index=6}

---

## 🧭 Threat model snapshot

A tiered architecture is only secure when tiers are **segregated** and trust relationships are treated as hostile-by-default. :contentReference[oaicite:7]{index=7}:contentReference[oaicite:8]{index=8}

### Trust boundaries (conceptual)

```mermaid
flowchart LR
  subgraph B[🌐 Browser / UI (Untrusted)]
    UI[Web App]
    LS[(Local Storage)]
  end

  subgraph S[🧱 API / Gatekeeper]
    API[FastAPI / REST / GraphQL]
    AUTHZ[AuthZ + Input Validation]
    RL[Rate Limits]
    LOG[Audit Logging]
  end

  subgraph D[🗄️ Data Zone]
    DB[(Postgres)]
    CAT[(Catalog: STAC/DCAT/PROV-O)]
    OBJ[(Tiles / Objects)]
  end

  UI -->|HTTPS| API
  API --> AUTHZ
  AUTHZ --> DB
  AUTHZ --> CAT
  AUTHZ --> OBJ
  API --> RL
  API --> LOG
  UI --> LS
```

- Server-side validation (e.g., Pydantic) is a core injection defense. :contentReference[oaicite:9]{index=9}
- The API should act as the **only** gatekeeper between client and data stores (no direct UI↔DB). :contentReference[oaicite:10]{index=10}

---

## 🏷️ Data classification model

KFM’s governance emphasizes consistent handling of sensitive information. A practical baseline classification model:

| Level | Who can access | Typical UI behavior | Notes |
|---|---|---|---|
| 🟢 **Public** | Everyone | Full render; shareable URLs | Open-by-default |
| 🟡 **Internal** | Authenticated users | Requires login; watermark optional | “Need-to-know” within org |
| 🟠 **Confidential** | Role-based users | Field/geometry redaction; export gated | Must log access |
| 🔴 **Restricted** | Selected users | Strong redaction; strict export rules | Highest sensitivity |

This aligns with an access policy / enforcement mechanism split (e.g., public = open, internal = login, confidential = role-based, restricted = selected). :contentReference[oaicite:11]{index=11}

> [!NOTE]
> Sensitive geospatial and community-protective policies (including CARE principles) should be treated as **first-class requirements**, not “optional governance.” :contentReference[oaicite:12]{index=12}

---

## 👤 Roles & permissions

The backend enforces roles + permissions (tokens + route guards). The UI mirrors those decisions for safer UX and less accidental exposure. :contentReference[oaicite:13]{index=13}

**Client-side policy helpers should:**
- Prefer **deny-by-default** if role/classification info is missing
- Provide **explainable** deny reasons (for support + governance)
- Emit audit/telemetry events when denying or redacting

> 🧩 Tier segregation matters: if one tier assumes another “already checked,” failures cascade. :contentReference[oaicite:14]{index=14}

---

## 🧾 Contract-first + provenance-first UI rules

KFM is designed around a “data contract” metadata JSON per dataset (source, license, extent, processing steps, etc.) and enforces a contract-first approach so components can rely on schema + provenance. :contentReference[oaicite:15]{index=15}

### What this means for this folder ✅
- **Every dataset/story/focus answer** should link back to its contract/provenance trail.
- UI should avoid displaying any layer without:
  - `source`
  - `license`
  - classification tag
  - processing lineage references  
  (otherwise: **treat as unsafe / block**)

---

## ✂️ Redaction & generalization pipeline

Redaction is not just deleting fields — it can include:
- **Attribute suppression**
- **Generalization** (rounding / binning)
- **Spatial generalization** (reduce coordinate precision, simplify geometry)
- **Aggregation** (minimum group sizes, safe summaries)

Privacy literature highlights that *outputs* can leak information and may require protections like k-anonymity variants, l-diversity, t-closeness, and **query auditing / inference control**. :contentReference[oaicite:16]{index=16}

### Suggested primitives (client-side)
- `redactFeature(feature, policy, ctx)`  
- `generalizeGeometry(geo, policy)`  
- `redactMarkdown(md, policy)`  
- `redactTable(rows, policy)`  
- `redactFocusAnswer(answer, citations, policy)`

### Telemetry examples
- `focus_mode_redaction_notice_shown`
- `data_export_redaction_applied`  
These “security events” support governance, incident response, and postmortems. :contentReference[oaicite:17]{index=17}

---

## 🧼 Safe rendering & UI hardening

KFM story content is authored in Markdown + JSON configs, and the front-end renders Markdown as HTML (sanitized). :contentReference[oaicite:18]{index=18}

### 🔥 Always treat as untrusted input
- Story Markdown
- Remote images and links
- User search text / filters
- Anything coming from external datasets
- Anything produced by an AI model (including citations)

### Baseline safeguards
- ✅ Sanitize Markdown → HTML
- ✅ Strict URL allowlist for external links
- ✅ Prevent tabnabbing: `rel="noopener noreferrer"`
- ✅ Escape any user-controlled strings used in attributes or URLs  
  (e.g., the general pattern of HTML-escaping URLs before embedding prevents URL-as-HTML injection). :contentReference[oaicite:19]{index=19}
- ✅ CSP + security headers belong at deploy edge / server, but this module can enforce safe defaults in rendering

---

## 🤖 Focus Mode AI security & integrity

Focus Mode is designed to produce **answers with references**, with output constrained toward known facts and clearly marked as AI-generated. :contentReference[oaicite:20]{index=20}

### UI responsibilities for Focus Mode
- **Show citations as clickable provenance links** (never “naked claims”)
- **Don’t render unsafe HTML** in AI output
- **Apply classification/redaction** to:
  - the question context
  - retrieved evidence
  - generated response

### Human-centered guardrails 🧑‍⚖️
Digital humanism work emphasizes the tension between **trust** and **transparency** in digital systems and the importance of clarity about what data is used and how. :contentReference[oaicite:21]{index=21}:contentReference[oaicite:22]{index=22}

---

## 🛰️ Observability, audit trails, and incident response

Backend guidance includes:
- input validation
- roles/permissions
- rate limiting
- request logging with unique IDs  
:contentReference[oaicite:23]{index=23}

Client-side should complement with:
- **security telemetry events** (blocked views, redaction applied, export attempted)
- **UI-level audit breadcrumbs** (what was shown, at what classification, under what context)
- **privacy-safe logging** (never log secrets; avoid high-resolution location traces unless explicitly permitted)

---

## 🚨 Vulnerability reporting & secure development workflow

KFM’s security governance includes **responsible disclosure** (no public exploit reports), private reporting channels, and automated tooling like Dependabot + audits and CodeQL. :contentReference[oaicite:24]{index=24}

### Expected repo docs (recommended)
- `SECURITY.md` (reporting, contact, PGP if used)
- `docs/security/` (threat model, incident response, policy)
- `docs/standards/` (cross-project conventions)

> [!TIP]
> “Documentation + best practices matter” is treated as part of the project’s disciplined research/engineering posture. :contentReference[oaicite:25]{index=25}

---

## ✅ PR checklist (security)

Before merging any PR that touches UI rendering, datasets, or Focus Mode:

- [ ] Classification is present and enforced (deny-by-default if missing)
- [ ] Redaction applied consistently (UI + exports + AI output)
- [ ] No new unsafe HTML sinks (innerHTML, unescaped attributes, etc.)
- [ ] Telemetry events added for sensitive flows
- [ ] Links are safe (`noopener`, allowlist, no open redirects)
- [ ] Tests cover the policy edge cases
- [ ] Dependency updates pass audits (JS + Python if applicable) :contentReference[oaicite:26]{index=26}

---

## 🗂️ Suggested internal layout (optional but recommended)

> This is a **recommended** breakdown if the folder grows.

```text
web/src/core/security/
  README.md
  policy/          # classification + policy evaluation
  auth/            # SecurityContext builders + token helpers
  redact/          # redaction + generalization utilities
  sanitize/        # markdown/html/url sanitizers
  telemetry/       # security event emitters + schemas
  types.ts         # shared types: Role, Classification, PolicyDecision
```

---

## 📚 Appendix: Project files used as the security knowledge base

<details>
<summary>📦 Click to expand the full project library index (mapped to security)</summary>

| Project file | Security relevance (how it informs this module) |
|---|---|
| **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf** | Provenance-first + contract-first trust model; front-end untrusted; security governance; Focus Mode w/ citations |
| **MARKDOWN_GUIDE_v13.md.gdoc** | Data sensitivity rules; redaction and “no output less restricted than input”; CARE principles; audit trails |
| **Data Spaces.pdf** | Trust, control, licensing constraints, access policy patterns; classification & enforcement framing |
| **Data Mining Concepts & applictions.pdf** | Output privacy risks; k-anonymity/l-diversity/t-closeness; query auditing & inference control |
| **S-T programming Books.pdf** | Tiered architecture risks; trust boundaries; defense-in-depth; RBAC patterns |
| **ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf** | Defensive mindset + countermeasure catalog (used only for hardening guidance) |
| **Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf** | Security awareness for reverse engineering & secure engineering (defensive takeaways) |
| **PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf** | Parameterization mindset, role hygiene, database-side least privilege implications |
| **Database Performance at Scale.pdf** | Security/performance tradeoffs (caching, observability, multi-tenant concerns) |
| **Scalable Data Management for Future Hardware.pdf** | Large-scale query processing patterns; risk-aware observability for analytics systems |
| **responsive-web-design-with-html5-and-css3.pdf** | Safer UI patterns; predictable rendering; avoiding brittle DOM security footguns |
| **webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf** | WebGL considerations (resource loading, origins, untrusted shaders/assets) |
| **compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf** | Secure handling of media inputs (size limits, content-type trust, parsing caution) |
| **python-geospatial-analysis-cookbook.pdf** | Geospatial processing context (privacy in coordinates; safe API boundaries) |
| **making-maps-a-visual-guide-to-map-design-for-gis.pdf** | Map communication ethics; how visual choices can unintentionally reveal sensitive info |
| **Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf** | Location privacy and socio-technical risks (mobile mapping as a sensitive surface) |
| **Archaeological 3D GIS_26_01_12_17_53_09.pdf** | Cultural heritage sensitivity patterns (site location risks, access gating) |
| **Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf** | Remote sensing sensitivity and derivative outputs (aggregation + disclosure risks) |
| **On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf** | AI governance/legal framing (accountability for AI outputs & data usage) |
| **Introduction to Digital Humanism.pdf** | Trust, transparency, human-centered constraints in AI + data systems |
| **Principles of Biological Autonomy - book_9780262381833.pdf** | System resilience thinking (security as an emergent property of control/feedback) |
| **Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf** | Verification mindset: testable assumptions, validation culture, reproducibility |
| **Spectral Geometry of Graphs.pdf** | Graph/knowledge structure context; integrity of relationships (anti-tamper mindset) |
| **Generalized Topology Optimization for Structural Design.pdf** | Engineering rigor mindset; reproducible pipelines |
| **Understanding Statistics & Experimental Design.pdf** | Safe experimentation and measurement for security UX changes (evidence-based) |
| **graphical-data-analysis-with-r.pdf** | Monitoring + anomaly visualization patterns for security telemetry |
| **think-bayes-bayesian-statistics-in-python.pdf** | Bayesian reasoning for risk scoring + alert triage |
| **regression-analysis-with-python.pdf** | Statistical modeling for anomaly detection and monitoring |
| **Regression analysis using Python - slides-linear-regression.pdf** | Quick reference for regression-based monitoring prototypes |
| **concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf** | Race-condition awareness; concurrency hazards feeding auth/session issues |
| **A programming Books.pdf** | Cross-language security patterns reference shelf |
| **B-C programming Books.pdf** | Cross-language security patterns reference shelf |
| **D-E programming Books.pdf** | Cross-language security patterns reference shelf |
| **F-H programming Books.pdf** | GIS query concepts (input validation awareness); baseline stats thinking |
| **I-L programming Books.pdf** | Cross-language security patterns reference shelf |
| **M-N programming Books.pdf** | Cross-language security patterns reference shelf |
| **O-R programming Books.pdf** | Output encoding patterns and safe URL/HTML handling |
| **U-X programming Books.pdf** | Cross-language security patterns reference shelf |
| **Deep Learning for Coders with fastai and PyTorch - Deep.Learning.for.Coders.with.fastai.and.PyTorchpdf** | ML safety mindset; data leakage awareness; model behavior constraints |

</details>

---

## 🧷 Glossary (quick)

- **AuthN**: Authentication (who are you?)
- **AuthZ**: Authorization (what can you do?)
- **RBAC**: Role-based access control
- **CSP**: Content Security Policy
- **XSS/CSRF**: common web threats to guard against
- **STAC / DCAT / PROV‑O**: catalog + dataset + provenance standards used for traceability :contentReference[oaicite:27]{index=27}

---

> ✅ If you’re adding anything new here, ask yourself:  
> **“Could this change let the UI output something less restricted than the input?”**  
> If yes: it’s a blocker until policy + tests + telemetry are in place. :contentReference[oaicite:28]{index=28}

