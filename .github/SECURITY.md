# 🛡️ Kansas Frontier Matrix (KFM) — Security, Safety & Governance Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)

![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![SLSA](https://img.shields.io/badge/SLSA-attestations%20%2B%20provenance-0f172a)
![Policy as Code](https://img.shields.io/badge/policy-as%20code-OPA%20%2B%20Conftest-111827)

![Kill Switch](https://img.shields.io/badge/safety-kill--switch%20%2B%20fail--closed-red)
![Contract First](https://img.shields.io/badge/data-contract--first-required-0ea5e9)
![Evidence Triplet](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-334155)
![Data Integrity](https://img.shields.io/badge/data-integrity-checksums%20%2B%20manifests-purple)

![AI Governance](https://img.shields.io/badge/AI-evidence--first%20%2B%20human--in--loop-8b5cf6)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE%20%2B%20cultural%20protocols-7c3aed)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling + narrative** system. Security issues can live in:
> **code**, **infra**, **catalog metadata (STAC/DCAT)**, **provenance (PROV)**, **data contracts**, **Story Nodes**, **3D/WebGL assets**, **offline packs**, and **AI/Focus Mode outputs**. 🧾🗺️🧠  
> Treat reports as potentially sensitive.

---

## ⚡ TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** + **Contract/STAC/DCAT/PROV paths**

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [🧭 Policy goals & principles](#-policy-goals--principles)
- [🧑‍⚖️ Governance model, roles & responsibilities](#️-governance-model-roles--responsibilities)
- [⭐ Security invariants](#-security-invariants)
- [🎯 Scope](#-scope)
- [🧩 Threat model (KFM-shaped)](#-threat-model-kfm-shaped)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & sensitive location policy](#-data-classification--sensitive-location-policy)
- [🧾 Metadata, provenance & data contract requirements](#-metadata-provenance--data-contract-requirements)
- [🪪 Identity, access & auditability](#-identity-access--auditability)
- [🔏 Artifact integrity, reproducibility & release discipline](#-artifact-integrity-reproducibility--release-discipline)
- [🤖 Focus Mode AI & automation security](#-focus-mode-ai--automation-security)
- [⚖️ Policy-as-code enforcement](#️-policy-as-code-enforcement)
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
| Last updated | **2026-01-19** |
| Review cycle | Quarterly 🔁 *(or after material security/governance changes)* |
| v13 alignment | ✅ `KFM_REDESIGN_BLUEPRINT_v13` + `MASTER_GUIDE_v13` conventions |
| Evidence profiles baseline | **KFM-STAC v11.0.0** · **KFM-DCAT v11.0.0** · **KFM-PROV v11.0.0** *(profiled standards for catalogs + lineage)* |
| Default posture | **Fail-closed** for promotion-critical gates 🚦 |
| Applies to | This repo + official releases + supported deployments + offline packs |
| “Metadata as code” posture | **Contracts + catalogs + provenance must validate** (CI gates) ✅ |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> Keep **one canonical** file; mirrors are allowed, but **drift is a security risk**.

---

## 🧭 Policy goals & principles

KFM’s security stance is shaped by geospatial realities, “evidence-first” system design, and human-centered governance.

### 🎯 What this policy optimizes for

- **Safety of people, places, and communities** 🧑‍🤝‍🧑🗺️  
  Especially for **cultural heritage and sensitive locations**, where map precision can cause real-world harm.
- **Trustworthy knowledge & narratives** 🧾✅  
  If it’s in the UI, Story Nodes, or Focus Mode, it must be **traceable, attributable, and reproducible**.
- **Supply-chain resilience (code + data)** 🔗🧱  
  Datasets + catalogs + provenance are treated like dependencies (SBOM/attestation mindset).
- **Operational containment & rollback** 🧯♻️  
  Incidents are expected; KFM is designed to **fail closed** and **roll back cleanly**.

### 🧠 “Security is not just AppSec” (KFM-specific)

In KFM, security includes:
- **Catalog integrity** *(STAC/DCAT link safety, schema correctness, licensing terms, domain allowlists)*
- **Provenance integrity** *(PROV + run records as audit trail + reproducibility)*
- **Modeling integrity** *(verification/validation/uncertainty labeling — V&V/UQ as risk reduction)*
- **Narrative integrity** *(Story Nodes must cite evidence; AI assistance must be labeled + provenance-linked)*
- **Cultural protocol integrity** *(CARE + community rules; prevent “open-by-default” harm)*

---

## 🧑‍⚖️ Governance model, roles & responsibilities

> [!NOTE]
> KFM is interdisciplinary: maintainers + data stewards + domain experts (historians, geographers, scientists) all contribute. Governance needs clear lanes. 🛤️

### 👤 Core roles (recommended)

- **Security Response Lead (SRL)** 🧯  
  Owns triage, incident coordination, advisory publishing, and vulnerability comms.
- **FAIR+CARE & Cultural Protocol Council** 🧾🌿🏷️  
  Owns data classification, sensitive location review, licensing/attribution, and cultural protocol requirements (e.g., TK labels).
- **Data Intake Steward** 🧰  
  Owns intake gates, contract/cat/prov validity, and “no mystery nodes” enforcement.
- **Release Manager** 📦  
  Owns signed releases, SBOM/attestations, and promotion lane gating.
- **Maintainers / Reviewers** 👀  
  Own branch protection enforcement and code/data review quality.
- **Deployment Operator (self-hosted installs)** 🧑‍💻  
  Owns runtime hardening, secrets management, monitoring, and incident containment actions.

### 🧾 Governance ledger (recommended)

Maintain a lightweight, append-only **governance ledger** (human approvals + hashes) for:
- Sensitive data approvals (who/when/why)
- Exceptions to default precision restrictions
- Takedown/restriction events + remediations
- Publication approvals for “high impact” releases (major datasets, new public layers, offline packs)

> [!TIP]
> Keep decisions in `docs/architecture/adr/` and approvals in `docs/guides/governance/` (or a dedicated ledger path) so governance doesn’t live only in tribal memory.

---

## ⭐ Security invariants

KFM’s architecture uses **non-negotiable invariants** that double as security controls (intended to be enforced by CI) ✅🤖

1) 🧬 **Pipeline ordering is absolute**  
**Raw → Work → Processed → Contract → (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
No stage consumes artifacts that haven’t passed the previous stage’s **formal outputs + checks**.

2) 🧾 **Contract-first + evidence-triplet is mandatory**  
If something shows up in the UI / Focus Mode, it must be traceable to:
- ✅ a **data contract** (schema + governance metadata)  
- ✅ the **evidence triplet**: **STAC + DCAT + PROV**  
No “mystery layers.” No “trust me bro.” 🚫

3) 🧊 **`data/raw` is immutable (append-only)**  
Raw intake is a **preservation zone**. Never rewrite raw inputs.  
Processing produces **new versions** (with new digests + PROV).

4) 🧪 **Deterministic, idempotent ETL**  
Same input + config ⇒ same output. Runs must be re-runnable safely.  
No partial publishes. No unreproducible outputs.

5) 🕸️ **Graph is derived, not hand-edited**  
The knowledge graph is built from validated catalogs/contracts/provenance (e.g., bulk CSV import snapshots).  
If the graph changes, the source artifacts must explain why.

6) 🔌 **API boundary rule**  
The UI must **never** talk to the graph DB or raw object storage directly.  
All access goes through governed APIs (authZ, redaction, schema contracts). 🔐

7) 🌿 **Sovereignty + classification propagate**  
No output artifact may be **less restricted** than its inputs.  
Redaction/generalization is required to publish sensitive inputs safely.

8) 🚦 **Fail-closed promotion gates**  
Missing provenance, broken catalogs, unsafe links, secrets, or sensitive precision leakage → **block merge/publish**.

9) 🎬 **Evidence-first narrative (Story Nodes)**  
No unsourced narrative content.  
Facts must cite evidence, and AI-assisted text must be labeled + provenance-linked.

10) 🤝 **Humans approve publishing**  
Automation may open PRs, run checks, and attach evidence — but merges/promotion remain governed and reviewable. 👀✅

> [!IMPORTANT]
> In KFM, **metadata is security-critical**. A broken catalog link, missing license, unsafe remote href, or unvalidated contract can become a supply-chain issue for downstream consumers.

---

## 🎯 Scope

KFM is a **geospatial + historical mapping + modeling platform** that typically includes:

- 🖥️ Web UI *(React; 2D MapLibre + 3D Cesium; story/narrative panels)*
- 📱 Mobile / PWA mode *(offline caching; field workflows; potential AR integration)*
- 🔌 APIs/services *(FastAPI + REST/GraphQL; policy-aware access control)*
- 🧰 Workers/pipelines *(ETL + analytics + publishing; deterministic jobs)*
- 🗄️ Spatial storage *(PostgreSQL/PostGIS)*
- 🕸️ Knowledge graph *(Neo4j; ontologies; citations)*
- 🪣 Object storage *(tiles, COGs, docs, artifacts, offline packs)*
- 🗂️ Catalog + provenance layer *(STAC/DCAT/PROV + contracts + evidence manifests)*
- 🤖 AI layer *(Focus Mode; optional agent workflows; PR-only execution)*
- 🧑‍🤝‍🧑 Collaboration features *(now: Git-based; future: in-app comments/annotations/moderation)*

### ✅ In-scope vulnerability examples

- AuthN/authZ bypass (including IDOR), privilege escalation
- Injection (SQL/command/graph query), SSRF, stored/reflected XSS, CSRF with real impact
- Unsafe file upload, path traversal, deserialization issues, RCE
- Secrets exposure (tokens/keys), sensitive data leakage (**including precise coordinates**)
- Supply-chain risks introduced by this repo (dependencies, CI scripts, GitHub Actions)
- Geo + graph specific:
  - **Catalog poisoning** (malicious STAC/DCAT links/fields) → unsafe fetches or consumer compromise
  - **Retrieval poisoning** (malicious citations/graph nodes influencing Focus Mode answers)
  - Integrity tampering of published assets (COGs/tiles/docs/model artifacts/offline packs)
  - “Geospatial DoS” payloads (massive geometries, decompression bombs, pathological tilesets) that crash pipelines/UI
  - Graph query complexity DoS (deep traversals, path explosion)

### ✅ Offline packs / mobile / AR are in scope

If KFM supports **offline data packs**, **PWA caching**, or **AR overlays**, vulnerabilities are in scope, including:
- Pack signature/attestation bypass
- Pack containing misclassified/restricted data
- Sensitive coordinate exposure via device caches
- Permission misuse (GPS/camera) or privacy leaks

---

## 🧩 Threat model (KFM-shaped)

KFM’s threat surface includes more than code.

### 🎯 Assets we protect
- 🔐 Credentials (cloud keys, DB creds, service tokens, CI secrets)
- 🧾 Contract + catalog integrity (Contracts/STAC/DCAT) + provenance integrity (PROV)
- 🗺️ Sensitive location data (protected/cultural sites, private infrastructure)
- 📦 Published artifacts (tiles/COGs/GeoJSON/GeoParquet, reports, model outputs, offline packs)
- 🎬 Narrative trust (Story Nodes/Focus Mode must be evidence-backed and labeled)
- 🤖 CI/CD supply chain (workflows/actions, artifact promotion, attestations)
- 🧑‍💻 User privacy (analytics/logs; accounts if enabled; moderation content)

### 👤 Likely threat actors
- Opportunistic attackers (common web vulns, exposed secrets, misconfig)
- Malicious data contributors (poisoning/tampering)
- Supply-chain attackers (dependencies/CI)
- Data scrapers targeting sensitive coordinates or operational details
- Well-meaning contributors who accidentally leak restricted data

### 🧨 Common KFM-specific failure modes
- “It’s just metadata” mindset → unsafe STAC/DCAT hrefs, licensing gaps, missing provenance
- UI bypassing the API boundary → authZ/redaction failure
- Pipelines fetching remote assets without allowlists → SSRF + internal exposure
- Publishing exact sensitive coordinates (maps, story text, exports, offline caches)
- Weak integrity controls → silent tampering, untraceable outputs
- LLM prompt injection / retrieval poisoning → untrusted text instructing Focus Mode to ignore rules
- Graph query/path explosion → DoS via overly deep traversals
- High-risk parsers (PDFs/images/3D assets) → decompression bombs / memory exhaustion
- Offline packs → restricted data “walks out the door” if misclassified or unsigned
- Automation without kill-switch → autopublish drift during an incident

> [!NOTE]
> KFM treats “trustworthy outputs” as a security property: verification/validation, uncertainty labeling, and reproducibility reduce both scientific and security risk.

---

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  EXT[🛰️ External Providers<br/>archives • APIs • feeds • GEE] -->|untrusted| INTAKE[🧰 Intake Gate<br/>contract + checksums]
  INTAKE --> RAW[(🧊 data/raw<br/>immutable)]
  RAW --> WORK[(🧪 data/work<br/>scratch)]
  WORK --> PROC[(📦 data/processed<br/>versioned outputs)]

  PROC --> EVID[🧾 Evidence Triplet<br/>STAC + DCAT + PROV]
  EVID --> GRAPH[(🕸️ Knowledge Graph<br/>Neo4j • CSV import)]
  EVID --> OBJ[(🪣 Object Storage<br/>tiles • COGs • docs)]
  GRAPH --> API[🔌 API / Services<br/>REST + GraphQL]
  OBJ --> API

  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI<br/>(MapLibre + Cesium)]
  FE -->|governed calls| API

  API --> AUTH[(🔐 AuthN/AuthZ<br/>RBAC + ABAC)]
  API --> PACK[📦 Offline Pack Builder<br/>(signed + attested)]
  PACK --> U
  API --> FM[🤖 Focus Mode Runtime<br/>(retrieval + citations)]
  FM --> GRAPH
  FM --> API
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

> [!IMPORTANT]
> Some datasets require **cultural protocols / indigenous data sovereignty constraints** beyond “Public vs Private.”  
> These must be encoded in contracts + catalogs and enforced at access time. 🌿🏷️

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

### 🛡️ Sensitive-location publishing defaults

- **Default deny** for “Exact” precision in Public.
- Prefer **grid/index** publication for public discovery.
- Require **explicit review** for any public release that could enable:
  - looting/vandalism (archaeology, cultural heritage)
  - targeting private infrastructure
  - harassment or stalking
- Add a **“location inference risk”** note when a dataset could be re-identified by joining layers.
- Prefer **rounding / jitter / aggregation** when appropriate (document the method + impact in PROV).

### 🏷️ Cultural protocol controls (recommended)

When a dataset involves cultural heritage, sacred sites, or community-governed knowledge:

- Encode protocol fields in the **contract** and **catalogs** (e.g., `cultural_protocols`, `tk_labels`, `authority_to_control`).
- Apply **access control beyond RBAC** (ABAC rules based on protocol tags).
- Provide “**why restricted**” user-facing explanations without revealing sensitive details.
- Require **Council sign-off** for any policy exceptions.
- Treat violations as security incidents.

### 🔐 Privacy and user logs (deployment-aware)

KFM deployments may collect logs/analytics. Treat those as potentially sensitive:
- **Data minimization**: log only what you need.
- **Pseudonymize** user identifiers where feasible.
- Restrict access to logs (often **Restricted**).

---

## 🧾 Metadata, provenance & data contract requirements

KFM treats metadata and lineage as **security controls**, not “nice-to-have docs.”

### ✅ Required boundary artifacts (publish bar)

Every dataset or evidence artifact that is promoted/published must have:

- 🧾 **Data contract JSON** *(KFM schema; includes license + classification + FAIR/CARE + cultural protocol flags where needed)*  
- 🧾 **STAC Collection + Item(s)** *(geospatial indexing + assets; include KFM profile fields like dataset ID + classification)*
- 🗃️ **DCAT dataset entry** *(discovery + distributions + license; include sovereignty/protocol metadata where applicable)*
- 🧬 **PROV lineage bundle** *(inputs → activities → outputs, with agents + parameters)*
- 🔎 **Cross-layer linkage** (bidirectional where possible):
  - Contract ↔ STAC ↔ DCAT ↔ PROV
  - Graph references catalogs/contracts (no bulky raw data embedded)

> [!IMPORTANT]
> If the contract, catalogs, or provenance don’t validate, **it does not ship**. 🚫📦

### 🗂️ Data contracts (KFM “metadata as code”)

A **data contract** is required for ingestion and promotion. It must include, at minimum:

- `id` *(stable, unique)*  
- `title`, `description`
- `license` + attribution fields
- `schema_version`
- spatial + temporal extent *(including CRS and any reprojection notes)*
- provenance sources + processing summary
- **classification** + sensitive location policy fields
- **FAIR+CARE** fields *(recommended)*
- **cultural protocol / sovereignty** fields *(when applicable)*
- **approvals** *(when applicable: e.g., IRB / institutional approvals / data use agreements)*

<details>
<summary><strong>🧾 Simplified contract example (shape only)</strong></summary>

```json
{
  "id": "usgs_historic_topo_1894",
  "title": "USGS Historical Topographic Map (Ellsworth County, 1894)",
  "description": "Digitized 1894 USGS topographic survey of Ellsworth County, Kansas.",
  "license": { "spdx": "PDDL-1.0", "notes": "Public domain (US Gov data)" },
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
  "governance": {
    "faircare": {
      "collective_benefit": "Preserves environmental and cartographic heritage of Kansas.",
      "authority_to_control": "Open",
      "responsibility": "Data Engineering & FAIR+CARE Council",
      "ethics": "Culturally neutral archival content"
    },
    "cultural_protocols": null,
    "approvals": []
  }
}
```

</details>

### 🗺️ Catalog paths (v13 guidance)

Pick **one canonical** layout and enforce it with policy to prevent drift:

- STAC: `data/stac/collections/` + `data/stac/items/` *(recommended canonical)*
- PROV: `data/prov/`
- DCAT: either `data/catalogs/` **or** `data/catalog/dcat/` *(choose one and enforce; do not allow both)*

> [!TIP]
> Directory drift is a real security risk: it can hide unvalidated artifacts and bypass gates.

### 🕸️ Knowledge graph integrity rules

- The graph is a **derived view** of governed artifacts.
- Prefer reproducible bulk import snapshots (e.g., `data/graph/csv/nodes.csv` and `data/graph/csv/edges.csv`).
- Use stable IDs, ontology alignment (e.g., CIDOC-CRM + GeoSPARQL + OWL-Time), and strict referential integrity checks.
- The graph must carry classification/protocol metadata so the API can enforce ABAC.

### 📦 Evidence artifacts (analysis/AI outputs)

Any analysis output or AI-generated dataset is treated as a **first-class dataset**:
- stored like a dataset
- cataloged like a dataset
- traced like a dataset
- exposed only via governed APIs (never hard-coded into the UI)

---

## 🪪 Identity, access & auditability

KFM assumes **role-based access** plus **attribute-based access** for classification and cultural protocols.

### 🧑‍💼 RBAC baseline roles (recommended)

| Role | Typical capabilities |
|---|---|
| **Public Viewer** 🌍 | Read Public datasets; view published stories; export public views |
| **Contributor** 🧑‍🔧 | Propose data/stories via PR; run local validators; cannot publish |
| **Maintainer** 👀 | Review + merge; trigger promotion lanes; cannot bypass gates |
| **Data Steward** 🧾🌿 | Approve classification/protocol changes; authorize exceptions |
| **Admin** 🧨 | Manage users/secrets; emergency actions; incident containment |

> [!IMPORTANT]
> “Contributor can upload but not publish without review” is a deliberate safety posture. ✅

### 🧷 ABAC requirements (classification-aware)

- Every request that returns data must enforce:
  - dataset `classification`
  - `sensitive_location_precision`
  - `cultural_protocols` / sovereignty tags
- The same ABAC rules apply to:
  - exports
  - offline pack builds
  - Story Node renders
  - Focus Mode evidence retrieval

### 🧾 Auditability expectations

- Privileged actions must be logged:
  - publish/promote
  - redact/remove
  - user/role changes
  - policy overrides
- Logs must be access-controlled and retained per deployment needs.

---

## 🔏 Artifact integrity, reproducibility & release discipline

KFM treats both **code** and **data** as a supply chain.

### 🔐 Integrity signals (recommended baseline)

- **Checksums/digests** (SHA-256) for artifacts and large assets
- **`checksums.sha256`** per dataset/work unit (or equivalent manifest)
- **`source.json`** *(or similar)* to record upstream URL, license, retrieved time, ETag/Last-Modified if available
- **Manifests** for dataset releases (files + hashes + contract/cat/prov IDs)
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
- classification + precision tier + protocol tags

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
  "policy": {
    "classification": "Public",
    "precision": "County / region"
  }
}
```

### 📦 Offline pack integrity (if supported)

Offline packs must be treated like releases:

- Packs must be **signed and attested** (build provenance + manifest)
- Packs must contain:
  - contract + catalogs + provenance for included datasets
  - a pack-level manifest listing hashes and classifications
  - explicit “what’s missing” if the online system has more restricted data
- Packs must be **policy-filtered** (ABAC must be applied before inclusion)
- Packs must support **revocation/expiry** strategies (deployment-dependent)

> [!CAUTION]
> Offline packs can quietly become the highest-risk distribution channel if misclassified data slips in. Treat them as “export on steroids.” 🧯

---

## 🤖 Focus Mode AI & automation security

Automation exists to reduce toil — **not** to bypass governance.

### 🧠 Focus Mode AI guardrails (non-negotiable)

- **Evidence-first retrieval**: Focus Mode relies on the graph + cataloged sources.
- **Citations required**: answers must cite contract/catalog/provenance-backed evidence.
- **Uncertainty over fabrication**: if evidence is missing, refuse or label uncertainty.
- **Policy-aware redaction**: classification + sensitive-location + cultural protocol rules apply at response time.
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
- 🧠 **Planner**: produces a deterministic plan (what will change and why) under policy constraints
- 🛠️ **Executor**: opens a PR with the change — **never auto-merges**

### ✅ Non-negotiables for automation

- 🧯 **Kill switch exists and is honored** everywhere (CI + agents + promotion jobs)
- 🔁 **Idempotency key + commit seed** recorded (replays produce identical results)
- 🧪 **Detect → Validate → Promote** discipline:
  - detect change robustly (checksums/ETags/events)
  - validate with fast gates + lane validators
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

### 🧾 Model cards & bias testing (recommended)

Any AI model used in production-facing features should ship with:
- model card (purpose, training data sources, limitations)
- evaluation summary (including bias checks if relevant)
- provenance record tying the model artifact to its data + code + config

---

## ⚖️ Policy-as-code enforcement

KFM governance rules should be enforceable by machines. 🧠✅

### ✅ OPA/Rego + Conftest (recommended)

Policy-as-code must cover:
- contract required fields
- catalog validity and link safety
- provenance required on publish
- classification propagation
- sensitive location precision rules
- workflow least privilege (CI)
- action pinning and dependency hygiene

> [!TIP]
> KFM references a **“policy pack”** concept. Keep it in a canonical location (e.g., `api/scripts/policy/` or `tools/validation/policy/`) and avoid duplicates.

### 🏷️ Example rule IDs (recommended style)

Use stable IDs for policy violations so CI output is actionable:

- `KFM-PROV-001`: Processed data changed without matching PROV update
- `KFM-CAT-002`: STAC/DCAT link domain not in allowlist (SSRF prevention)
- `KFM-CLASS-001`: Output classification lower than input classification
- `KFM-STORY-001`: Story markdown contains unsafe HTML / injection risk
- `KFM-PACK-001`: Offline pack includes Restricted/Confidential data

---

## ✅ Supported versions

We prioritize fixes for actively developed code and active public distributions.

| Target | Supported for security fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Latest data catalog / pack release | ✅ | If distributed publicly |
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
- **Affected component(s)** (UI/API/DB/pipelines/catalogs/CI/Focus Mode/offline packs)
- **Safe proof of concept** *(non-destructive, no public exploit chains)*
- **Suggested fix** *(optional)*
- **Version/commit** tested
- **Environment** (OS/browser/runtime/container tags)

### 🧭 KFM-specific context that helps a lot
- Dataset IDs (e.g., `kfm.ks.<domain>.<layer>.<time>.vN`)
- Contract paths: `docs/data/contracts/**`
- STAC paths: `data/stac/**`
- DCAT paths: `data/catalogs/**` *(or `data/catalog/dcat/**` if that’s your canonical layout)*
- PROV paths: `data/prov/**`
- Graph snapshot paths: `data/graph/csv/**` *(if applicable)*
- Whether the issue leaks **exact coordinates** vs redacted/generalized outputs
- Whether the issue could be:
  - **catalog poisoning** (unsafe `links[].href`)
  - **retrieval poisoning** (graph nodes/docs altering Focus Mode behavior)
  - **offline pack leakage** (device storage, caches, pack manifest issues)

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
- Graph snapshot (if applicable):
- Offline pack involved? (Y/N)
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
- offline pack accidentally includes restricted datasets

**How to request a takedown / restriction change**
- Preferred: private vulnerability report (Security tab) labeled **“DATA TAKEDOWN / SENSITIVE DATA”**
- Include:
  - dataset ID(s)
  - contract ID(s) + classification + protocol tags
  - where it’s published (STAC/DCAT links, UI pages, offline pack name)
  - why it must be restricted/removed
  - requested remediation (remove, redact, generalize, move to private, revoke pack)

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
- Render Story Node Markdown with a sanitizer (deny raw HTML by default)
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

### ⚙️ Pipeline & worker safety (race conditions + resource safety)
- Make pipeline runs idempotent; avoid partial publishes
- Use staging directories + atomic “commit” step
- Run decoders/parsers with guardrails (size limits, timeouts)
- Treat ZIPs, PDFs, images, and large geometries as hostile until validated
- Avoid downloading arbitrary remote URLs; use allowlists + SSRF defenses

### 📦 Offline pack safety (if supported)
- Packs must be signed + attested and include a manifest
- Packs must be policy-filtered and never include Restricted data
- Pack UI should show “classification + provenance” banners even offline
- Prefer encryption at rest on device (deployment-dependent)

### ♻️ Dependency & CI supply-chain hygiene
- Use lockfiles (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, etc.)
- Keep dependencies updated; avoid abandoned packages
- Pin base images; rebuild regularly
- Pin GitHub Actions by commit SHA when feasible
- Generate SBOMs for releases (recommended)

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
- Link-check critical `links[].href` (prevents “catalog poisoning” + SSRF)
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- “Classification propagation” checks (prevent public publish of restricted inputs)
- Raster/vector safety checks (size limits, geometry validity, decompression defenses)
- Story Node lint:
  - markdown sanitization (deny raw HTML by default)
  - ensure referenced layer IDs exist
  - link safety checks
  - citations present for claims (policy-driven)

### ⚖️ Governance gates via policy-as-code
Use **OPA/Rego** via **Conftest** (or equivalent) to enforce “default deny” rules.

<details>
<summary><strong>📁 Suggested policy pack layout</strong></summary>

```text
📁 api/scripts/policy/            # (canonical in v13 docs) OR mirror in tools/validation/policy/
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
│  │  ├─ 📄 cultural_protocols.rego
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

</details>

Example Conftest call (shape only — adapt to your repo layout):

```bash
conftest test \
  --policy api/scripts/policy/rego \
  --all-namespaces \
  docs/data/contracts/ data/stac/ data/prov/ .github/workflows/
```

### 🔏 Supply-chain controls (recommended for releases; optional for PRs)
- SBOM generation (SPDX/CycloneDX)
- Build provenance attestations (GitHub attestations / Sigstore-ish)
- Reproducibility lane compares rebuilt hashes
- Signed tags/releases (where feasible)

---

## 🚨 Incident response expectations

KFM treats these as security incidents:
- secrets exposure
- sensitive location publication
- cultural protocol violation (unauthorized access/disclosure)
- catalog poisoning / unsafe remote fetch behavior
- retrieval poisoning that affects Focus Mode trust
- integrity tampering of published artifacts/offline packs
- unauthorized access to DB/storage/graph
- compromised CI runners or supply-chain breakage

### ✅ Minimum expectations (for maintainers)

- **Containment first**:
  - flip kill-switch
  - restrict access / revoke tokens
  - disable promotions (fail-closed)
  - pause offline pack distribution (if applicable)
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

---

## 🗂️ Recommended repo security files

<details>
<summary><strong>📁 Suggested layout (v13-friendly)</strong></summary>

```text
📦 .github/
 ├─ 📄 dependabot.yml
 ├─ 📄 CODEOWNERS
 ├─ 📁 workflows/
 │  ├─ 📄 ci.yml
 │  ├─ 📄 codeql.yml
 │  ├─ 📄 contract-validate.yml
 │  ├─ 📄 catalog-qa.yml
 │  ├─ 📄 policy-gate.yml
 │  ├─ 📄 sbom.yml
 │  └─ 📄 attest.yml

📦 docs/
 ├─ 📁 architecture/
 │  ├─ 📁 adr/
 │  └─ 📄 KFM_REDESIGN_BLUEPRINT_v13.md
 ├─ 📁 guides/
 │  └─ 📁 governance/
 │     ├─ 📄 faircare-oversight.md
 │     └─ 📄 cultural-protocols.md
 ├─ 📁 security/
 │  ├─ 📄 incident-response.md
 │  ├─ 📄 secrets-policy.md
 │  ├─ 📄 threat-model.md
 │  └─ 📄 pgp-public-key.asc
 └─ 📁 data/
    └─ 📁 contracts/
       ├─ 📁 examples/
       └─ 📄 schema.json

📦 api/
 └─ 📁 scripts/
    └─ 📁 policy/                   # policy pack (OPA/Rego + tests)

📦 tools/
 └─ 📁 validation/
    ├─ 📁 contract_validate/
    ├─ 📁 catalog_qa/
    └─ 📁 policy/                   # optional mirror (avoid drift)

📦 data/
 ├─ 📁 raw/                         # immutable
 ├─ 📁 work/
 ├─ 📁 processed/
 ├─ 📁 stac/
 │  ├─ 📁 collections/
 │  └─ 📁 items/
 ├─ 📁 prov/
 ├─ 📁 catalogs/                    # OR 📁 catalog/dcat/ (pick one)
 └─ 📁 graph/
    └─ 📁 csv/

📦 .kfm/
 └─ 📄 kill-switch.yml
```

</details>

---

## 📚 Project reference library

> [!NOTE]
> These project files inform KFM’s defensive posture (governance, integrity, reproducibility, performance, privacy, and secure engineering).  
> They are **not** a request for offensive tooling contributions. 🚫🧨

### 🧭 Core KFM system documentation
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- 📄 `Kansas Frontier Matrix – Comprehensive UI System Overview.pdf`
- 📄 `📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf`
- 📄 `🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf`
- 📄 `Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf`

### 📦 Reference bundles (PDF portfolios; multi-book)
- 📚 `AI Concepts & more.pdf` *(digital humanism, accountability, AI governance framing)*
- 📚 `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(data management + CI/CD + cryptography references)*
- 📚 `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(GIS ethics + WebGL/3D + archaeology sensitivity)*
- 📚 `Various programming langurages & resources 1.pdf` *(secure implementation references; defensive awareness)*

<details>
<summary><strong>🧠 Why keep these bundles?</strong></summary>

They serve as a shared reference shelf for:
- threat modeling + secure engineering habits
- location privacy and cultural sensitivity
- data integrity, provenance, and reproducibility discipline
- secure UI and WebGL asset handling

</details>

---

## 🧾 Appendix: Checklists & templates

### ✅ PR checklist (maintainers & contributors)

- [ ] No secrets committed (checked)
- [ ] Contract JSON updated/added (if data changed)
- [ ] STAC/DCAT/PROV updated/added (if publishable artifact changed)
- [ ] Graph snapshot regenerated (if relevant) and derived from governed artifacts
- [ ] Classification + sensitive precision reviewed (if location data present)
- [ ] Cultural protocol tags reviewed (if applicable)
- [ ] Link safety (no unsafe remote hrefs)
- [ ] Tests + validation gates passing
- [ ] Story content is sanitized + cites evidence (if Story Nodes changed)
- [ ] Focus Mode prompts/rules unchanged or reviewed (if AI layer touched)
- [ ] Offline pack changes reviewed + signed/attested (if applicable)

### ✅ “Ready to publish” checklist (promotion lane)

- [ ] All CI gates passing (contract + catalogs + provenance + policy)
- [ ] SBOM generated (software)
- [ ] Attestation generated (build provenance)
- [ ] Dataset DBOM manifests present (data releases)
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