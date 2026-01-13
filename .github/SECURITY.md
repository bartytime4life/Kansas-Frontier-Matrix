# 🛡️ Kansas Frontier Matrix (KFM) — Security, Safety & Governance Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)
![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![Policy as Code](https://img.shields.io/badge/policy-as%20code-OPA%20%2B%20Conftest-111827)
![Kill Switch](https://img.shields.io/badge/safety-kill--switch%20%2B%20fail--closed-red)
![Contract First](https://img.shields.io/badge/data-contract--first-required-0ea5e9)
![Data Integrity](https://img.shields.io/badge/data-integrity-PROV%20%2B%20checksums-purple)
![Catalogs](https://img.shields.io/badge/catalog-STAC%20%2B%20DCAT-334155)
![AI Governance](https://img.shields.io/badge/AI-evidence--first%20%2B%20human--in--loop-8b5cf6)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7c3aed)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling** system — security issues can live in **code**, **infrastructure**, **catalog metadata (STAC/DCAT)**, **provenance (PROV)**, **data contracts**, **documents**, **3D/WebGL assets**, and **derived outputs** (models / Story Nodes / Focus Mode).  
> Treat reports as potentially sensitive. 🧾🗺️🧠

---

## ⚡ TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** + **Contract/STAC/DCAT/PROV paths**

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [🧭 Policy goals & principles](#-policy-goals--principles)
- [🧑‍⚖️ Roles & responsibilities](#️-roles--responsibilities)
- [⭐ Security invariants](#-security-invariants)
- [🎯 Scope](#-scope)
- [🧩 Threat model (KFM-shaped)](#-threat-model-kfm-shaped)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & sensitive location policy](#-data-classification--sensitive-location-policy)
- [🧾 Metadata, provenance & data contract requirements](#-metadata-provenance--data-contract-requirements)
- [🔏 Artifact integrity, reproducibility & release discipline](#-artifact-integrity-reproducibility--release-discipline)
- [🤖 Focus Mode AI & automation security](#-focus-mode-ai--automation-security)
- [✅ Supported versions](#-supported-versions)
- [🐛 Reporting a vulnerability](#-reporting-a-vulnerability)
- [🧾 What to include](#-what-to-include)
- [🗺️ Dataset / sensitive data takedown requests](#-dataset--sensitive-data-takedown-requests)
- [🗞️ Advisories & notifications](#-advisories--notifications)
- [⏱️ Coordinated disclosure](#-coordinated-disclosure)
- [🧭 Safe harbor](#-safe-harbor)
- [🚫 Out of scope](#-out-of-scope)
- [🧰 Secure development guidelines](#-secure-development-guidelines)
- [🧪 Security gates in CI](#-security-gates-in-ci)
- [🚨 Incident response expectations](#-incident-response-expectations)
- [🗂️ Recommended repo security files](#-recommended-repo-security-files)
- [📚 Project reference library](#-project-reference-library)
- [🧾 Appendix: Checklists & templates](#-appendix-checklists--templates)

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| Policy file | `SECURITY.md` *(canonical location: repo root **or** `.github/` — pick one and avoid drift)* |
| Status | Active ✅ |
| Last updated | **2026-01-13** |
| Review cycle | Quarterly 🔁 *(or after material security changes)* |
| KFM-MDP baseline | **v11.2.6** |
| Master Guide baseline | **v13 (draft)** |
| Governance baseline | FAIR + CARE *(data + people)* |
| Default posture | **Fail-closed** for promotion-critical gates 🚦 |
| Applies to | This repo + official releases + supported deployments |
| “Metadata as code” posture | **Contracts + catalogs must validate** (CI gates) ✅ |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> Keep **one canonical** file; mirrors are allowed, but **drift is a security risk**.

---

## 🧭 Policy goals & principles

KFM’s security stance is shaped by the project’s “NASA‑grade” modeling discipline, geospatial realities, and human-centered governance.

### 🎯 What this policy is optimizing for

- **Safety of people, places, and communities** 🧑‍🤝‍🧑🗺️  
  Especially for **cultural heritage and sensitive locations**, where map precision can cause real-world harm.
- **Trustworthy knowledge** 🧾✅  
  If it’s in the UI, Story Nodes, or Focus Mode, it must be **traceable, attributable, and reproducible**.
- **Supply-chain resilience** 🔗🧱  
  Datasets + catalogs + provenance are treated like dependencies (SBOM/attestation mindset).
- **Operational containment** 🧯  
  Incidents are expected; KFM is designed to **fail closed** and **rollback cleanly**.

### 🧠 “Security is not just AppSec” (KFM-specific)

In KFM, security includes:
- **Catalog integrity** *(STAC/DCAT link safety, schema correctness, licensing terms)*  
- **Provenance integrity** *(PROV + run records as audit trail)*  
- **Modeling integrity** *(verification/validation/uncertainty — V&V/UQ)*  
- **Narrative integrity** *(Story Nodes must cite evidence and label AI assistance)*  

---

## 🧑‍⚖️ Roles & responsibilities

> [!NOTE]
> KFM is interdisciplinary: maintainers + data stewards + domain experts (historians, geographers, scientists) all contribute. Governance needs clear lanes. 🛤️

### 👤 Core roles (recommended)

- **Security Response Lead (SRL)** 🧯  
  Owns triage, incident coordination, advisory publishing.
- **Data Steward / FAIR+CARE Council** 🧾🌿  
  Owns data classification, sensitive location review, licensing/attribution compliance.
- **Release Manager** 📦  
  Owns signed releases, SBOM/attestations, and promotion lane gating.
- **Maintainers / Reviewers** 👀  
  Own branch protection enforcement and code/data review quality.

### ✅ Required decisions to document

- Adding/removing maintainers (and required access levels)
- Promotion lane rules (what can publish, where, and how)
- Sensitive data release exceptions (with review record)

> [!TIP]
> Keep these decisions in `docs/architecture/adr/` (Architecture Decision Records) so governance doesn’t live only in tribal memory.

---

## ⭐ Security invariants

KFM’s architecture uses **non-negotiable invariants** that double as security controls (and are intended to be enforced by CI) ✅🤖:

1) 🧬 **Pipeline ordering is absolute**  
**ETL → Contracts → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
No stage consumes artifacts that haven’t passed the previous stage’s **formal outputs + checks**.

2) 🧾 **Contract-first & provenance-first is mandatory**  
If something shows up in the UI / Focus Mode, it must be traceable to:
- ✅ a **data contract** (schema + governance metadata)  
- ✅ a **catalog entry** (STAC/DCAT)  
- ✅ a **lineage record** (PROV)  
No “mystery layers.” No “trust me bro.” 🚫

3) 🔌 **API boundary rule**  
The UI must **never** talk to the graph DB or raw object storage directly.  
All access goes through governed APIs (authZ, redaction, schema contracts). 🔐

4) 🧾 **Boundary artifacts are security-critical**  
Before any dataset/evidence is “published,” it must have:
- 🧾 **STAC** (collections/items) for geospatial indexing
- 🗃️ **DCAT** for discovery/distribution
- 🧬 **PROV** for lineage (inputs → activities → outputs, with agents)
- 🧾 **Contract JSON** (schema + license + classification + FAIR/CARE)
- 🧪 **Integrity signals** *(recommended)*: checksums/digests, stable IDs, manifests  
If it’s visible downstream, it must be **cataloged + governed + traceable**.

5) ♻️ **Deterministic, idempotent ETL**  
Same input + config ⇒ same output. Runs must be re-runnable safely.  
No partial publishes. No unreproducible outputs. 🧪

6) 🧭 **Sovereignty & classification propagate**  
No output artifact may be **less restricted** than its inputs.  
Redaction/generalization is required to publish sensitive inputs safely. ⚖️✅

7) 🚦 **Fail-closed validation gates**  
Missing provenance, broken catalogs, unsafe links, secrets, or sensitive precision leakage → **block merge/publish**. 🧯

8) 🎬 **Evidence-first narrative**  
No unsourced narrative content in Story Nodes or Focus Mode.  
Facts must cite evidence, and AI-assisted text must be labeled + provenance-linked.

9) 🤝 **Humans approve publishing**  
Automation may open PRs, run checks, and attach evidence — but merges/promotion remain governed and reviewable. 👀✅

10) 🧠 **Focus Mode constraints reduce hallucination risk**  
Focus Mode must be constrained to **KFM’s graph + cataloged sources** and produce **citations**.  
If a claim isn’t supported by KFM evidence → it should be framed as uncertainty or omitted. ✅📎

> [!IMPORTANT]
> In KFM, **metadata is security-critical**. A broken catalog link, missing license, unsafe remote href, or unvalidated contract can become a supply-chain issue for downstream consumers.

---

## 🎯 Scope

KFM is a **geospatial + historical mapping + modeling platform** that typically includes:

- 🖥️ Web UI *(including WebGL/3D viewers)*
- 🔌 APIs/services *(e.g., FastAPI, REST/GraphQL)*
- 🧰 Workers/pipelines *(ETL + analytics + publishing)*
- 🗄️ Spatial storage *(PostgreSQL/PostGIS)*
- 🪣 Object storage *(rasters/COGs, tiles, docs, artifacts)*
- 🕸️ Knowledge graph *(entities/events/citations)*
- 🗂️ Catalog + provenance layer *(STAC/DCAT/PROV + data contracts)*
- 📓 Notebooks / research artifacts *(if in repo)*
- 🤖 Automation *(GitHub Actions, agents, promotion pipelines)*

### ✅ In-scope vulnerability examples

- AuthN/authZ bypass (including IDOR), privilege escalation
- Injection (SQL/command/graph query), SSRF, stored/reflected XSS, CSRF with real impact
- Unsafe file upload, path traversal, deserialization issues, RCE
- Secrets exposure (tokens/keys), sensitive data leakage (**including precise coordinates**)
- Supply-chain risks introduced by this repo (dependencies, CI scripts, GitHub Actions)
- Geo + graph specific:
  - **Catalog poisoning** (malicious STAC/DCAT links/fields) → unsafe fetches or consumer compromise
  - **Retrieval poisoning** (malicious citations/graph nodes influencing Focus Mode answers)
  - Integrity tampering of published assets (COGs/tiles/docs/model artifacts)
  - “Geospatial DoS” payloads (massive geometries, decompression bombs, pathological tilesets) that crash pipelines/UI
  - Graph query complexity DoS (deep traversals, path explosion)

---

## 🧩 Threat model (KFM-shaped)

KFM’s threat surface includes more than code.

### 🎯 Assets we protect
- 🔐 Credentials (cloud keys, DB creds, service tokens, CI secrets)
- 🧾 Contract + catalog integrity (Contracts/STAC/DCAT) + provenance integrity (PROV)
- 🗺️ Sensitive location data (protected/cultural sites, private infrastructure)
- 📦 Published artifacts (tiles/COGs/GeoJSON/GeoParquet, reports, model outputs)
- 🎬 Narrative trust (Story Nodes/Focus Mode must be evidence-backed and labeled)
- 🤖 CI/CD supply chain (workflows/actions, artifact promotion, attestations)
- 🧑‍💻 User privacy (analytics/logs, especially for authenticated deployments)

### 👤 Likely threat actors
- Opportunistic attackers (common web vulns, exposed secrets, misconfig)
- Malicious data contributors (poisoning/tampering)
- Supply-chain attackers (dependencies/CI)
- Data scrapers targeting sensitive coordinates or operational details
- Well-meaning contributors who accidentally leak restricted data

### 🧨 Common KFM-specific failure modes
- “It’s just metadata” mindset → unsafe STAC/DCAT hrefs, licensing gaps, missing provenance
- UI directly contacting internal stores/graph → bypassing authZ/redaction
- Pipelines fetching remote assets without allowlists → SSRF + internal exposure
- Publishing exact sensitive coordinates in public layers/story content
- Weak artifact integrity controls → silent tampering, untraceable outputs
- LLM prompt injection / retrieval poisoning → untrusted text instructing Focus Mode to ignore rules
- Graph query/path explosion → DoS via overly deep traversals
- High-risk parsers (PDFs/images/3D assets) → decompression bombs / memory exhaustion
- Automation without kill-switch → autopublish drift during an incident

> [!NOTE]
> KFM treats “trustworthy outputs” as a security property: verification/validation, uncertainty labeling, and reproducibility reduce both scientific and security risk.

---

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI<br/>(incl. WebGL/3D)]
  FE -->|governed calls| API[🔌 API / Services]
  API --> AUTH[(🔐 AuthN/AuthZ<br/>RBAC/ABAC)]
  API --> DB[(🗄️ Spatial DB<br/>PostgreSQL/PostGIS)]
  API --> GRAPH[(🕸️ Knowledge Graph<br/>entities • events • citations)]
  API --> OBJ[(🪣 Object Storage<br/>tiles • COGs • docs • artifacts)]
  API --> FM[🤖 Focus Mode Runtime<br/>(retrieval + citations)]
  FM -->|retrieval| GRAPH
  FM -->|evidence fetch| API

  API --> W[⚙️ Workers / Pipelines]
  W --> OBJ
  W --> EXT[🛰️ External Providers<br/>GIS APIs • archives • feeds • GEE]
```

</details>

> [!IMPORTANT]
> Anything crossing a trust boundary must assume **untrusted input** until validated  
> (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses, PDFs, images, and 3D assets). 🚧

---

## 🔒 Data classification & sensitive location policy

KFM is “mostly open” — but **not everything should be public**.

### 🧭 Recommended classification levels

| Classification | Who can access | Typical examples |
|---|---|---|
| **Public** 🌍 | Everyone | Published layers with clear licensing |
| **Internal** 🏢 | Maintainers/collaborators | Draft catalogs, staging pipelines, runbooks |
| **Confidential** 🔐 | Explicitly approved | Sensitive layers requiring controlled sharing |
| **Restricted** 🧨 | Admin/Owners only | Credentials, security logs, protected exact coordinates |

### 🧬 Propagation rule (non-negotiable)

**No output artifact can be less restricted than its inputs.**  
If a source is sensitive, all derivatives inherit equal-or-higher restrictions unless explicitly reviewed and redacted. ⚖️✅

### 🗺️ Sensitive location precision tiers (recommended)

| Precision tier | Examples | Allowed in Public? |
|---|---|---|
| **Exact** 🎯 | point GPS, parcel centroid, address-level | ❌ unless explicitly permitted |
| **Neighborhood / small area** 🧭 | 0.5–2km buffers | ⚠️ only with governance approval |
| **County / region** 🗺️ | county polygon, watershed, broad bbox | ✅ typically safe |
| **Grid / index** 🧊 | H3 / geohash cells | ✅ commonly safe if size is appropriate |
| **Redacted** 🕳️ | “location protected” + narrative context | ✅ preferred for cultural sensitivity |

> [!IMPORTANT]
> **Archaeological & cultural heritage locations** often require stricter handling.  
> Even “historic” sites can be vulnerable to looting or vandalism if precise coordinates are published.

### 🛡️ Sensitive-location publishing rules (recommended defaults)

- **Default deny for “Exact”** precision in Public.
- Prefer **grid/index** publishing for public discovery.
- Require **explicit review** for any public release that could enable:
  - looting/vandalism (archaeology, cultural heritage)
  - targeting private infrastructure
  - harassment or stalking
- Add a **“location inference risk”** note when a dataset could be re-identified by joining layers.

### 🔐 Privacy and user logs (deployment-aware)

KFM deployments may collect logs/analytics. Treat those as potentially sensitive:
- **Data minimization**: log only what you need.
- **Pseudonymize** user identifiers in logs where feasible.
- Restrict access to logs (often **Restricted**).

> [!TIP]
> If you implement “privacy protecting logs,” consider a one-way pseudonymous identifier (hashing a stable tuple) so operational analysis is possible without storing raw PII.

---

## 🧾 Metadata, provenance & data contract requirements

KFM treats metadata and lineage as **security controls**, not “nice-to-have docs.”

### ✅ Required boundary artifacts (publish bar)

Every dataset or evidence artifact that is promoted/published must have:

- 🧾 **Data contract JSON** *(KFM schema; includes license + classification + FAIR/CARE)*  
- 🧾 **STAC Collection + Item(s)** *(geospatial indexing + assets)*
- 🗃️ **DCAT dataset entry** *(discovery + distributions)*
- 🧬 **PROV lineage bundle** *(inputs → activities → outputs, with agents)*
- 🔎 **Cross-layer linkage**:
  - Contract ↔ STAC ↔ DCAT ↔ PROV (bidirectional where possible)
  - Graph entries reference catalogs (not bulky raw data)

### 🗂️ Data contracts (KFM “metadata as code”)

A **data contract** is required for ingestion and promotion. It must include, at minimum:

- `id` (stable, unique)
- `title`, `description`
- `license` + attribution fields (where applicable)
- `schema_version`
- spatial + temporal extent
- provenance source(s) + processing summary
- **classification** + sensitive location policy fields *(recommended)*
- **FAIR+CARE** fields *(recommended for governance transparency)*

<details>
<summary><strong>🧾 Simplified contract example (shape only)</strong></summary>

```json
{
  "id": "usgs_historic_topo_1894",
  "title": "USGS Historical Topographic Map (Ellsworth County, 1894)",
  "description": "Digitized 1894 USGS topographic survey of Ellsworth County, Kansas.",
  "license": "Public Domain",
  "schema_version": "v3.0.0",
  "classification": "Public",
  "sensitive_location_precision": "County / region",
  "spatial": { "bbox": [-99.5, 38.3, -98.8, 38.9], "crs": "EPSG:4326" },
  "temporal": { "start": "1894-01-01", "end": "1894-12-31" },
  "provenance": {
    "source_url": "https://www.usgs.gov/historical-topo",
    "creator": "U.S. Geological Survey",
    "issued": "1894-03-15"
  },
  "faircare": {
    "collective_benefit": "Preserves environmental and cartographic heritage of Kansas.",
    "authority_to_control": "Open",
    "responsibility": "Data Engineering & FAIR+CARE Council",
    "ethics": "Culturally neutral archival content"
  }
}
```

</details>

> [!IMPORTANT]
> If the contract, catalogs, or provenance don’t validate, **it does not ship**.

### 📦 Evidence artifacts (analysis/AI outputs)

Any analysis output or AI-generated dataset is treated as a **first-class dataset**:
- stored like a dataset
- cataloged like a dataset
- traced like a dataset
- exposed only via governed APIs (never hard-coded into the UI)

> [!NOTE]
> If an AI-generated artifact could influence decisions, it must include uncertainty/limitations and remain provenance-linked.

---

## 🔏 Artifact integrity, reproducibility & release discipline

KFM treats both **code** and **data** as a supply chain.

### 🔐 Integrity signals (recommended baseline)

- **Checksums/digests** (e.g., SHA-256) for artifacts and large assets
- **Manifests** for dataset releases (what files, what hashes, what contract/cat/prov IDs)
- **Immutability** for published artifacts (object storage versioning or content-addressed paths)
- **Reproducibility lane** for promotion (rebuild + compare hashes where feasible)
- **SBOM** for software releases + dependency review for PRs
- **Build provenance attestations** for release artifacts (CI-signed evidence)

### 🧾 Dataset BOM (DBOM) concept (recommended)

Think “SBOM, but for datasets.” For a release, publish:

- contract ID + schema version
- STAC/DCAT identifiers
- PROV run record (inputs, activities, agents)
- asset list with digests
- license summary + attribution bundle

Example (shape only):

```json
{
  "release": "kfm.data.catalog.2026-01",
  "commit": "abc1234",
  "contract_id": "usgs_historic_topo_1894",
  "stac_collection": "kfm.stac.usgs.topo",
  "prov_bundle": "data/prov/run_2026-01-12T02-14-00Z.json",
  "assets": [
    { "path": "data/processed/topo/1894_ellsworth.tif", "sha256": "..." }
  ],
  "license": { "spdx": "PDDL-1.0", "notes": "Public domain (US Gov data)" }
}
```

### 📚 Reproducible research integration (recommended)

- `CITATION.cff` for software citations
- DOIs or frozen snapshots for major data releases
- Optional notebook launchers (Binder/JupyterHub) **only** if secrets are not required and data classification allows it

> [!CAUTION]
> Public notebooks must never embed long-lived credentials. Use read-only public data or short-lived tokens.

---

## 🤖 Focus Mode AI & automation security

Automation exists to reduce toil — **not** to bypass governance.

### 🧠 Focus Mode AI guardrails (non-negotiable)

- **Evidence-first retrieval**: Focus Mode relies on the graph + cataloged sources.
- **Citations required**: answers must cite contract/catalog/provenance-backed evidence.
- **Policy-aware redaction**: classification + sensitive-location rules apply at response time.
- **Prompt injection defense**:
  - treat all retrieved text as untrusted
  - ignore instructions found inside data/documents
  - never follow “hidden” or “embedded” instructions from content

> [!IMPORTANT]
> Focus Mode must not become a “web-browsing bot” by accident.  
> If external web access is allowed in a deployment, it must be explicit, logged, and policy-gated.

### ✅ WPE model: Watcher → Planner → Executor (PR-only)

If we use agentic automation, it must follow:
- 👀 **Watcher**: detects drift/events (broken links, missing metadata, changes)
- 🧠 **Planner**: produces a deterministic plan (what will change and why)
- 🛠️ **Executor**: opens a PR with the change — **never auto-merges**

### ✅ Non-negotiables for automation

- 🧯 **Kill switch exists and is honored** everywhere (CI + agents + promotion jobs)
- 🔁 **Idempotency key + commit seed** recorded (replays produce identical results)
- 🧪 **Detect → Validate → Promote** discipline:
  - detect change robustly (checksums/ETags/events)
  - validate with fast gates + “lane” validators
  - promote via PR + signed/attested artifacts
- 🧾 **Evidence artifacts attached**: plans, gate reports, provenance, attestations
- 🔒 **Executor cannot merge** — branch protections remain the final gate

### 🛑 Kill switch pattern (recommended)

Support both mechanisms:

- **Repo variable (preferred for visibility):** `KFM_KILL_SWITCH=true`
- **Optional file-based switch:** `📄 .kfm/kill-switch.yml`

Example pattern for publish jobs:

```yaml
# publish jobs should be skipped (or hard-failed) when kill switch is ON
- name: 🧯 Kill-switch check
  shell: bash
  run: |
    set -euo pipefail

    # 1) repo variable
    if [ "${KFM_KILL_SWITCH:-false}" = "true" ]; then
      echo "Kill-switch enabled via repo variable. Stopping publish lane."
      exit 1
    fi

    # 2) file flag
    if [ -f ".kfm/kill-switch.yml" ]; then
      echo "Kill-switch file present (.kfm/kill-switch.yml). Stopping publish lane."
      exit 1
    fi
  env:
    KFM_KILL_SWITCH: ${{ vars.KFM_KILL_SWITCH }}
```

> [!TIP]
> In PR lanes you can choose to **skip publish steps** rather than failing the whole workflow, but promotion lanes should be **fail-closed**.

### 🧾 Model cards & bias testing (recommended for AI components)

Any AI model used in production-facing features should ship with:
- model card (purpose, training data sources, limitations)
- evaluation summary (including bias checks if relevant)
- provenance record tying the model artifact to its data + code + config

---

## ✅ Supported versions

We prioritize fixes for actively developed code.

| Target | Supported for security fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Older releases | ⚠️ Best effort | Fixes may not be backported |

---

## 🐛 Reporting a vulnerability

### ✅ Preferred: GitHub Private Vulnerability Reporting

1. Go to this repository’s **Security** tab  
2. Click **Report a vulnerability**  
3. Provide details (see the checklist below)

Direct route (repo-specific):
- `https://github.com/bartytime4life/Kansas-Frontier-Matrix/security/advisories/new`

> [!NOTE]
> If a security report is accidentally posted publicly, maintainers may **edit/remove** it to reduce exposure, then ask you to re-submit privately.

### 📧 Alternative: security contact (fallback)

If GitHub private reporting is not available:

- 📧 **Security email:** `security@YOUR-DOMAIN.example` *(maintainers: replace with a real monitored inbox)*  
- 🔐 **PGP key (recommended):**
  - 📁 `docs/security/`
    - 📄 `pgp-public-key.asc`
  - Fingerprint: `XXXX XXXX XXXX XXXX XXXX  XXXX XXXX XXXX XXXX XXXX`

> [!CAUTION]
> Avoid sending secrets in plaintext. If you must include credentials for reproduction:
> - use short-lived test creds  
> - label them **“TEMP FOR REPRO ONLY”**  
> - include revocation instructions

### 🧯 Suspected active exploitation?

If you believe there is **active exploitation** or imminent risk:
- Report privately immediately
- Include **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title
- If safe: include redacted logs/IoCs and scope estimates

---

## 🧾 What to include

To speed up triage, include:

- **Summary** (what is vulnerable?)
- **Impact** (what can an attacker do?)
- **Attack scenario** (realistic path)
- **Reproduction steps** (minimal)
- **Affected component(s)** (UI/API/DB/pipelines/catalogs/CI/Focus Mode)
- **Safe proof of concept** *(non-destructive, no public exploit chains)*
- **Suggested fix** *(optional)*
- **Version/commit** tested
- **Environment** (OS/browser/runtime/container tags)

### 🧭 KFM-specific context that helps a lot
- Dataset IDs (e.g., `kfm.ks.<domain>.<layer>.<time>.vN`)
- Contract paths: `docs/data/contracts/**` or `docs/data/contracts/examples/**`
- STAC paths: `data/stac/**` *(or `data/catalog/stac/**` if that’s canonical)*
- DCAT paths: `data/catalog/dcat/**`
- PROV paths: `data/prov/**`
- Whether the issue leaks **exact coordinates** vs redacted/generalized outputs
- Whether the issue could be:
  - **catalog poisoning** (unsafe `links[].href`)
  - **retrieval poisoning** (graph nodes/docs altering Focus Mode behavior)

### 🧾 Copy/paste report template

```text
Title:
Severity guess (optional):
Component(s):
Tested version/commit:
Environment:

Summary:
Impact:
Attack scenario:

Reproduction steps:
1)
2)
3)

Proof of concept (safe):
Expected result:
Actual result:

KFM-specific context (if relevant):
- Dataset ID(s):
- Contract/STAC/DCAT paths or IDs:
- PROV run record:
- Does it expose sensitive coordinates? (Y/N)

Suggested fix (optional):

Notes:
- Auth required? Y/N
- User interaction required? Y/N
- Network: public/private/internal-only
- Data exposure: metadata/PII/secrets/infra access
```

---

## 🗺️ Dataset / sensitive data takedown requests

Sometimes the risk is **data**, not code:
- license/attribution problems
- accidental publication of sensitive coordinates
- inclusion of culturally sensitive data without approval
- misclassified artifacts (public when they should be restricted)
- archaeology/cultural heritage location exposure

**How to request a takedown / restriction change**
- Preferred: private vulnerability report (Security tab) labeled **“DATA TAKEDOWN / SENSITIVE DATA”**
- Include:
  - dataset ID(s)
  - contract ID(s) + classification
  - where it’s published (STAC/DCAT links)
  - why it must be restricted/removed
  - requested remediation (remove, redact, generalize, move to private)

> [!IMPORTANT]
> We treat sensitive-location mistakes as **security incidents** (containment + remediation), not “content disagreements.” 🧯

---

## 🗞️ Advisories & notifications

We use GitHub security tooling when available:
- 🧾 **GitHub Security Advisories** for private triage + coordinated disclosure
- 📦 **Tagged releases** for patched versions (when applicable)

How to stay informed:
- ⭐ Watch this repo for **Releases**
- 🔔 Subscribe to advisories when published

> [!NOTE]
> We avoid publishing exploit details before a fix is available (unless otherwise agreed).

---

## ⏱️ Coordinated disclosure

We follow coordinated disclosure:

- 📩 **Acknowledgement**: confirm receipt promptly  
- 🔎 **Triage & validation**: reproduce + assess  
- 🛠️ **Fix & test**: patch + regression coverage  
- 📣 **Release & advisory**: disclose with mitigations  

### ⏳ Target response timelines (guidance)

| Stage | Target |
|---|---|
| Initial acknowledgement | **≤ 2 business days** |
| Triage started | **≤ 7 days** |
| Fix ETA communicated | **after validation** |
| Patch release (Critical/High) | **as fast as feasible** |
| Patch release (Medium/Low) | **scheduled / best effort** |

### 🏷️ Severity rubric (quick)

| Severity | Examples |
|---|---|
| **Critical** | RCE, auth bypass, secrets exfiltration, full DB compromise |
| **High** | privilege escalation, SSRF into internal services, major sensitive data exposure |
| **Medium** | stored XSS with meaningful impact, IDOR with limited scope |
| **Low** | minor info leaks, non-exploitable misconfigurations |

> [!TIP]
> If you have a CVSS vector/score (v3.1 or v4.0), include it (optional). We’ll still apply our own assessment.

---

## 🧭 Safe harbor

We support good‑faith security research that is:
- ✅ Non-destructive
- ✅ Minimal necessary testing
- ✅ Avoids privacy violations and data exfiltration
- ✅ Reported privately with reasonable detail

**Please do not:**
- ❌ Disrupt service (DoS / load testing) without explicit permission
- ❌ Access or modify data that isn’t yours
- ❌ Attempt social engineering (phishing, impersonation)
- ❌ Publish details before a patch is available (unless otherwise agreed)

> [!IMPORTANT]
> If you follow this policy in good faith, we consider your actions authorized and we will not pursue legal action against you for accidental, good‑faith violations. If unsure, **stop and report privately**.

---

## 🚫 Out of scope

- Issues requiring **physical access** to devices
- **Denial of Service** via high-traffic/brute-force load testing
- Vulnerabilities **only in upstream providers** (report upstream), unless KFM configuration makes them exploitable
- Automated scanner output **without** actionable context or plausible impact

Usually out of scope unless chained:
- Missing headers without exploitability
- Clickjacking on non-sensitive pages
- Open redirects with no meaningful impact
- Self-XSS without a privilege chain

---

## 🧰 Secure development guidelines

Security is a design constraint, not a patch. 🧱

### 🔑 Secrets & credentials
- Never commit secrets (`.env`, keys, tokens, credentials)
- Use `.env` locally + `.gitignore`
- Prefer secret stores in production (GitHub Secrets/Environments, vaults, cloud secret managers)
- Rotate anything potentially exposed
- Treat logs as sensitive; avoid printing tokens/PII
- Prefer short-lived credentials (OIDC → cloud) where possible

### 🌐 Web/UI security (including WebGL & 3D)
- Validate inputs on **server** (client validation is UX, not security)
- Encode outputs; avoid unsafe HTML injection
- Use secure cookies, CSRF protections where relevant, and a strict CSP
- Treat 3D assets (glTF/3D Tiles/etc.) as untrusted input
- Keep CORS least-privilege (avoid `*` with credentials)
- Set request size limits (GeoJSON uploads, shader strings, style JSON, etc.)

> [!CAUTION]
> WebGL + large assets can crash GPUs/browsers. Enforce size limits, progressive loading, and resource budgets.

### 🔌 API/service security
- AuthN + AuthZ for all sensitive routes
- RBAC/ABAC as needed (classification-aware)
- Rate limit expensive endpoints (exports, deep graph traversals, heavy spatial queries)
- Request/response schema validation (OpenAPI contracts)
- Audit logging for privileged actions (publish, promote, redact, delete)
- “Default deny” for promotion endpoints

### 🕸️ Knowledge graph security
- Parameterized graph queries (avoid string concatenation)
- Query budgets:
  - max depth / hop count
  - max results
  - timeouts
- Guard against path-explosion DoS
- Separate read/write roles; restrict administrative procedures
- Ensure graph ↔ catalog referential integrity checks are enforced

### 🗄️ Database security (PostgreSQL/PostGIS)
- Separate read/write roles (and separate migration role if possible)
- Use parameterized queries everywhere (no string-built SQL)
- Enable TLS for DB connections; avoid “trust without verification”
- Use timeouts:
  - `statement_timeout`
  - `lock_timeout`
- Validate geometry (types, SRID, bounds) before insert
- Rate-limit expensive geospatial queries and exports
- Backups encrypted; restore paths audited

> [!TIP]
> If you must use connection pooling, ensure pool configs don’t weaken security (e.g., verify TLS certs, don’t disable validation).

### ⚙️ Pipeline & worker safety (race conditions + resource safety)
- Make pipeline runs idempotent; avoid partial publishes
- Use staging directories + atomic “commit” step
- Run decoders/parsers with guardrails (size limits, timeouts)
- Treat ZIPs, PDFs, images, and large geometries as hostile until validated
- Avoid downloading arbitrary remote URLs; use allowlists + SSRF defenses

### 🛰️ External providers & live feeds (remote sensing, archives, APIs)
- Restrict API keys/service accounts by least privilege
- Separate “build” vs “publish” permissions
- Validate external inputs (bounds, schema, CRS, expected ranges)
- Treat external JSON/GeoJSON feeds as untrusted (SSRF + poisoning risks)
- Don’t embed long-lived credentials in notebooks or exports

### 🧠 Modeling, simulation & ML/analytics integrity
- Track dataset provenance, versions, checksums (poisoning defense)
- Separate train/eval/test; avoid leakage in artifacts
- Report uncertainty and limitations (avoid “false certainty”)
- Store model cards/experiment logs for any published ML output
- Be mindful of model inversion/membership inference for exposed models
- Prefer reproducible pipelines (seeded randomness, recorded configs)

### 🗺️ Cartography & map output safety (trust-by-design)
- Avoid misleading symbology; document scale/resolution limits
- Clearly label projections, uncertainty, and “modeled vs observed”
- For sensitive topics: prefer aggregation, redaction, or grid publication

### ♻️ Dependency & CI supply-chain hygiene
- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin base images; rebuild regularly
- Pin GitHub Actions by commit SHA when feasible
- Generate SBOMs for releases (recommended)

### 🐳 Container & runtime hardening
- Run as non-root where possible
- Minimize image size (multi-stage builds)
- Don’t bake secrets into images
- Use read-only filesystems where feasible
- Treat CI runners as sensitive infrastructure

---

## 🧪 Security gates in CI

Security must be repeatable and boring. ✅

### ✅ Code security (baseline)
- CodeQL scanning (SAST)
- Dependency Review (PRs)
- Secret scanning + push protection (repo settings)
- Lint/typecheck/tests as required checks
- Container scanning (recommended)

### 🗂️ Contract/catalog/data integrity checks (geo-specific)
- **Contract validator gate** (JSON schema, required governance fields)
- STAC/DCAT quick gate (required fields, license/providers/extensions)
- Link-check critical `links[].href` (prevents “catalog poisoning”)
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- “Classification propagation” checks (prevent public publish of restricted inputs)
- Raster/vector safety checks (size limits, geometry validity, decompression defenses)

### ⚖️ Governance gates (FAIR + CARE) via policy-as-code
Use **OPA/Rego** policies via **Conftest** to enforce “default deny” rules for governed surfaces.

✅ Recommended policy tool home:

```text
📁 tools/validation/policy/
├─ 📄 README.md
├─ 📁 rego/
│  ├─ 📁 common/
│  │  ├─ 📄 helpers.rego
│  │  ├─ 📄 license_allowlist.rego
│  │  └─ 📄 url_allowlist.rego
│  ├─ 📁 contracts/
│  │  ├─ 📄 contract_required.rego
│  │  └─ 📄 classification_required.rego
│  ├─ 📁 catalogs/
│  │  ├─ 📄 stac_required.rego
│  │  ├─ 📄 dcat_required.rego
│  │  ├─ 📄 prov_required.rego
│  │  └─ 📄 link_safety.rego
│  ├─ 📁 governance/
│  │  ├─ 📄 classification_propagation.rego
│  │  ├─ 📄 sensitive_locations.rego
│  │  └─ 📄 attribution.rego
│  ├─ 📁 supply_chain/
│  │  ├─ 📄 workflows_least_privilege.rego
│  │  └─ 📄 actions_pinning.rego
│  └─ 📄 bundles.rego
└─ 📁 tests/
   ├─ 📄 *_test.rego
   └─ 📁 samples/
      ├─ 📁 good/
      └─ 📁 bad/
```

Example Conftest call (shape only — adapt to your repo layout):

```bash
conftest test \
  --policy tools/validation/policy/rego \
  --all-namespaces \
  docs/data/contracts/ data/ .github/workflows/ .github/actions/
```

### 🔏 Supply-chain controls (recommended for releases; optional for PRs)
- SBOM generation (SPDX/CycloneDX)
- Build provenance attestations (GitHub attestations / Sigstore-ish)
- Reproducibility lane compares rebuilt hashes
- Signed tags/releases (where feasible)

> [!TIP]
> Treat “promotion” as the safe boundary: **validate → attest → publish atomically**, rollback-ready. 🧯

---

## 🚨 Incident response expectations

KFM treats these as security incidents:
- secrets exposure
- sensitive location publication
- catalog poisoning / unsafe remote fetch behavior
- retrieval poisoning that affects Focus Mode trust
- integrity tampering of published artifacts
- unauthorized access to DB/storage/graph
- compromised CI runners or supply-chain breakage

### ✅ Minimum expectations (for maintainers)

- **Containment first**:
  - flip kill-switch
  - restrict access / revoke tokens
  - disable promotions (fail-closed)
- **Preserve evidence**:
  - keep logs, artifacts, provenance records (don’t destroy audit trails)
- **Correct the catalogs/contracts**:
  - remove/disable affected STAC/DCAT entries
  - invalidate unsafe external links
  - correct misclassification and republish redacted outputs
- **Patch & validate**:
  - fix root cause
  - add regression tests + policy rules
  - rerun gates
- **Document**:
  - short incident note (private if needed)
  - public advisory if appropriate

> [!NOTE]
> Data takedowns (sensitive coordinates, restricted archives) should follow incident handling, even if no attacker is involved.

---

## 🗂️ Recommended repo security files

<details>
<summary><strong>📁 Suggested layout (v13-friendly)</strong></summary>

```text
📦 .github/
 ├─ 📄 SECURITY.md                       # (optional mirror) policy copy
 ├─ 📄 dependabot.yml
 ├─ 📄 CODEOWNERS
 ├─ 📁 workflows/
 │  ├─ 📄 ci.yml
 │  ├─ 📄 codeql.yml
 │  ├─ 📄 contract-validate.yml          # contract schema + governance checks
 │  ├─ 📄 catalog-qa.yml                 # STAC/DCAT quick gate + link safety
 │  ├─ 📄 policy-gate.yml                # Conftest/OPA gate for governed surfaces
 │  ├─ 📄 sbom.yml                       # SBOM generation (release lane)
 │  └─ 📄 attest.yml                     # provenance/build attestations (release lane)
 └─ 📁 actions/
    ├─ 📁 check-kill-switch/             # fail-closed stop button helper
    ├─ 📁 policy-gate/                   # conftest wrapper + bundles
    ├─ 📁 contract-validate/             # contract validator wrapper
    ├─ 📁 catalog-qa/                    # fast STAC/DCAT checks wrapper
    ├─ 📁 sbom/                          # SBOM helper
    └─ 📁 attest/                        # attestation helper

📦 tools/
 └─ 📁 validation/
    ├─ 📁 contract_validate/             # JSON schema + CLI validator
    ├─ 📁 catalog_qa/
    └─ 📁 policy/                        # OPA policies + tests (see tree above)

📦 docs/
 ├─ 📁 architecture/
 │  └─ 📁 adr/
 ├─ 📁 security/
 │  ├─ 📄 incident-response.md
 │  └─ 📄 pgp-public-key.asc
 ├─ 📁 ethics/
 ├─ 📁 review/
 ├─ 📁 data/
 │  └─ 📁 contracts/
 │     ├─ 📁 examples/
 │     └─ 📄 schema.json
 └─ 📁 library/                          # defensive references + GIS + modeling discipline

📦 data/
 ├─ 📁 raw/
 ├─ 📁 work/
 ├─ 📁 processed/
 ├─ 📁 stac/                              # or 📁 data/catalog/stac/ (pick one canonical)
 ├─ 📁 catalog/
 │  └─ 📁 dcat/
 └─ 📁 prov/

📦 notebooks/                             # (optional) research notebooks (no secrets)

📦 .kfm/
 └─ 📄 kill-switch.yml                    # optional file-based fail-closed switch
```
</details>

---

## 📚 Project reference library

> [!NOTE]
> These project files inform KFM’s defensive posture (governance, integrity, reproducibility, performance, privacy, and secure engineering).  
> They are **not** a request for offensive tooling contributions. 🚫🧨

### 🧠 Modeling, simulation, and scientific rigor
- 📄 `Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf` — verification/validation, uncertainty, reproducibility discipline
- 📄 `Understanding Statistics & Experimental Design.pdf` — experimental rigor, bias reduction, valid inference
- 📄 `graphical-data-analysis-with-r.pdf` — trustworthy exploratory analysis + visualization hygiene
- 📄 `regression-analysis-with-python.pdf` — regression pitfalls, leakage, reproducible modeling
- 📄 `Regression analysis using Python - slides-linear-regression.pdf` — modeling fundamentals + assumptions reminders
- 📄 `think-bayes-bayesian-statistics-in-python.pdf` — uncertainty-aware reasoning and probabilistic reporting

### 🗺️ GIS, cartography, remote sensing, and location ethics
- 📄 `python-geospatial-analysis-cookbook.pdf` — CRS/geometry validation patterns + geospatial tooling discipline
- 📄 `making-maps-a-visual-guide-to-map-design-for-gis.pdf` — map design ethics, legibility, and “don’t mislead”
- 📄 `Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf` — location privacy + societal impacts
- 📄 `Cloud-Based Remote Sensing with Google Earth Engine-Fundamentals and Applications.pdf` — remote sensing pipelines + provider integration considerations
- 📄 `Archaeological 3D GIS_26_01_12_17_53_09.pdf` — cultural heritage sensitivity and precision risk

### 🗄️ Data management, databases, and scale
- 📄 `PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf` — roles, auth, TLS, safe DB usage patterns
- 📄 `Database Performance at Scale.pdf` — query budgets, timeouts, performance-as-resilience
- 📄 `Scalable Data Management for Future Hardware.pdf` — scaling patterns (caching, batching) with governance caveats
- 📄 `Data Spaces.pdf` — access control, data classification, privacy-aware logging, federated governance patterns

### 🌐 Web, visualization, and asset safety
- 📄 `responsive-web-design-with-html5-and-css3.pdf` — UI engineering patterns + secure-by-default front-end habits
- 📄 `webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf` — WebGL pipelines; treat shaders/assets as untrusted
- 📄 `compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf` — image parsing realities; decompression/memory safety mindset

### 🔐 Security & systems engineering mindset
- 📄 `ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf` — defensive network security patterns and threat awareness
- 📄 `Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf` — reinforces “untrusted input” thinking for binary/assets (defensive use only)
- 📄 `concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf` — concurrency hazards (deadlocks/races) relevant to pipelines/workers

### 🕸️ Graphs, optimization, and algorithmic complexity
- 📄 `Spectral Geometry of Graphs.pdf` — graph algorithm complexity; motivates query budgets and DoS defenses
- 📄 `Generalized Topology Optimization for Structural Design.pdf` — heavy compute workflows; motivates resource guardrails and reproducibility

### 🧑‍🤝‍🧑 Digital humanism, ethics, and governance
- 📄 `Introduction to Digital Humanism.pdf` — human-centered governance, transparency, accountability
- 📄 `On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf` — accountability, explainability, prediction vs “prophecy” risks
- 📄 `Principles of Biological Autonomy - book_9780262381833.pdf` — autonomy + boundaries; caution against “control fallacies” in system design

### 🧰 Programming compendiums (multi-book collections)
> [!TIP]
> These are “binder PDFs” containing many language/runtime references used for secure implementation details and CI scripting hygiene.

- 📄 `A programming Books.pdf`
- 📄 `B-C programming Books.pdf`
- 📄 `D-E programming Books.pdf`
- 📄 `F-H programming Books.pdf`
- 📄 `I-L programming Books.pdf`
- 📄 `M-N programming Books.pdf`
- 📄 `O-R programming Books.pdf`
- 📄 `S-T programming Books.pdf`
- 📄 `U-X programming Books.pdf`

### 🧾 KFM primary system documentation
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf` — contract-first/provenance-first architecture, Focus Mode/Story Nodes, federation roadmap

---

## 🧾 Appendix: Checklists & templates

### ✅ PR checklist (maintainers & contributors)

- [ ] No secrets committed (checked)
- [ ] Contract JSON updated/added (if data changed)
- [ ] STAC/DCAT/PROV updated/added (if publishable artifact changed)
- [ ] Classification and sensitive precision reviewed (if location data present)
- [ ] Link safety (no unsafe remote hrefs)
- [ ] Tests + validation gates passing
- [ ] Story content cites evidence (if Story Nodes changed)
- [ ] Focus Mode prompt/rules unchanged or reviewed (if AI layer touched)

### ✅ “Ready to publish” checklist (promotion lane)

- [ ] All CI gates passing (contract + catalogs + provenance + policy)
- [ ] SBOM generated (software)
- [ ] Attestation generated (build provenance)
- [ ] Dataset BOM manifests present (data releases)
- [ ] Release notes include security + governance changes (if any)
- [ ] Kill switch verified OFF (or publish lane must block)

---

<!--
Maintainers’ TODOs (keep this short and actionable):
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add PGP key at 📁 docs/security/📄 pgp-public-key.asc and publish its fingerprint.
- Add incident-response runbook: containment, comms, logging, recovery, postmortem.
- Wire CI gates: CodeQL, dependency review, secret scanning, container scanning, contract validation, STAC/DCAT/PROV validation, policy-gate, story-lint.
- Keep OPA/Conftest policies tested (good/bad samples) and deny-by-default for promotion.
- Ensure kill switch is implemented and honored by all publish/sign workflows and agents.
-->