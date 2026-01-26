# 🛡️ Kansas Frontier Matrix (KFM) — Security, Safety & Governance Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)

![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![SLSA](https://img.shields.io/badge/SLSA-provenance%20%2B%20attestations-0f172a)
![Sigstore](https://img.shields.io/badge/Sigstore-Cosign%20signing-111827)
![Policy as Code](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20Conftest-111827)

![Fail Closed](https://img.shields.io/badge/posture-fail--closed-critical)
![Kill Switch](https://img.shields.io/badge/safety-kill--switch%20%2B%20rollback-red)
![Contract First](https://img.shields.io/badge/contracts-contract--first-required-0ea5e9)
![Evidence Triplet](https://img.shields.io/badge/evidence-STAC%20%2B%20DCAT%20%2B%20PROV-334155)

![FAIR+CARE](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7c3aed)
![Sovereignty](https://img.shields.io/badge/governance-sovereignty%20%2B%20cultural%20protocols-6d28d9)
![AI Governance](https://img.shields.io/badge/AI-evidence--first%20%2B%20HITL-8b5cf6)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling + narrative** system. Security issues can live in:
> **code**, **infra**, **catalog metadata (STAC/DCAT)**, **provenance (PROV)**, **contract artifacts**, **Story Nodes**, **3D/WebGL assets**, **offline packs**, **federated artifacts**, **notebooks**, and **AI/Focus Mode outputs**. 🧾🗺️🧠  
> Treat reports as potentially sensitive.

---

## ⚡ TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** + **artifact paths** (`STAC/DCAT/PROV/contract/schema`)

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [🧭 Goals & principles](#-goals--principles)
- [🧑‍⚖️ Governance model, roles & responsibilities](#️-governance-model-roles--responsibilities)
- [⭐ Security invariants](#-security-invariants)
- [🎯 Scope](#-scope)
- [🧩 Threat model](#-threat-model)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & sensitive location policy](#-data-classification--sensitive-location-policy)
- [🧾 Contracts, catalogs & provenance requirements](#-contracts-catalogs--provenance-requirements)
- [🪪 Identity, access & auditability](#-identity-access--auditability)
- [🔏 Artifact integrity, reproducibility & release discipline](#-artifact-integrity-reproducibility--release-discipline)
- [🌐 Federation & cross-instance security](#-federation--cross-instance-security)
- [🤖 Focus Mode AI & automation security](#-focus-mode-ai--automation-security)
- [⚖️ Policy-as-code enforcement](#️-policy-as-code-enforcement)
- [🧰 Secure development guidelines](#-secure-development-guidelines)
- [🧪 Security gates in CI](#-security-gates-in-ci)
- [🚨 Incident response expectations](#-incident-response-expectations)
- [✅ Supported versions](#-supported-versions)
- [🐛 Reporting a vulnerability](#-reporting-a-vulnerability)
- [🧾 What to include](#-what-to-include)
- [🗺️ Dataset / sensitive data takedown requests](#-dataset--sensitive-data-takedown-requests)
- [🗞️ Advisories & notifications](#-advisories--notifications)
- [⏱️ Coordinated disclosure](#️-coordinated-disclosure)
- [🧭 Safe harbor](#-safe-harbor)
- [🚫 Out of scope](#-out-of-scope)
- [🗂️ Recommended repo security files](#️-recommended-repo-security-files)
- [📚 Project reference library](#-project-reference-library)
- [🧾 Appendix: Checklists & templates](#-appendix-checklists--templates)

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| Policy file | **`.github/SECURITY.md`** *(canonical for v13; avoid drift)* |
| Status | Active ✅ |
| Last updated | **2026-01-26** |
| Review cycle | Quarterly 🔁 *(or after material security/governance changes)* |
| Architecture alignment | ✅ **v13** pipeline invariants *(contract-first + evidence-first + API-boundary)* |
| Evidence profiles baseline | **KFM-STAC v11.x** · **KFM-DCAT v11.x** · **KFM-PROV v11.x** *(profiled standards for catalogs + lineage)* |
| Default posture | **Fail-closed** for promotion-critical gates 🚦 |
| Applies to | This repo + official releases + supported deployments + offline packs + federated artifacts |
| “Metadata as security” posture | **Contracts + catalogs + provenance must validate** (CI gates) ✅ |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> **Pick one canonical location** (we do: **`.github/SECURITY.md`**) and enforce it.

---

## 🧭 Goals & principles

KFM’s stance is shaped by geospatial realities, “evidence-first” system design, and human-centered governance.

### 🎯 What this policy optimizes for

- **Safety of people, places, and communities** 🧑‍🤝‍🧑🗺️  
  Especially for **cultural heritage and sensitive locations**, where map precision can cause real-world harm.
- **Trustworthy knowledge & narratives** 🧾✅  
  If it’s in the UI, Story Nodes, notebooks, or Focus Mode, it must be **traceable, attributable, and reproducible**.
- **Supply-chain resilience (code + data + models)** 🔗🧱  
  Datasets and derived artifacts are treated like dependencies (SBOM/DBOM + provenance/attestation mindset).
- **Operational containment & rollback** 🧯♻️  
  Incidents are expected; KFM is designed to **fail closed**, **pause promotion**, and **roll back cleanly**.
- **Governance as a runtime capability** ⚖️  
  Rules are versioned, enforced, auditable, and adjustable without “hand-waving” exceptions.

### 🧠 “Security is not just AppSec” (KFM-specific)

In KFM, security includes:

- **Catalog integrity** *(STAC/DCAT link safety, schema correctness, license terms, domain allowlists)*
- **Provenance integrity** *(PROV + run records as audit trail + reproducibility)*
- **Modeling integrity** *(verification/validation + uncertainty labeling as risk reduction)*
- **Narrative integrity** *(Story Nodes cite evidence; AI assistance is labeled + provenance-linked)*
- **Sovereignty + cultural protocol integrity** *(CARE + community rules; prevent “open-by-default” harm)*
- **Federation integrity** *(only import/share attested artifacts + policy-compatible metadata)*

---

## 🧑‍⚖️ Governance model, roles & responsibilities

> [!NOTE]
> KFM is interdisciplinary: maintainers + data stewards + domain experts (historians, geographers, scientists) all contribute. Governance needs clear lanes. 🛤️

### 👤 Core roles (recommended)

- **Security Response Lead (SRL)** 🧯  
  Owns triage, incident coordination, advisory publishing, and vulnerability comms.
- **Governance Council (FAIR+CARE + Sovereignty)** 🧾🌿🏷️  
  Owns data classification, sensitive location review, licensing/attribution, and cultural protocol requirements.
- **Policy Owner (OPA/Rules Maintainer)** ⚖️  
  Owns policy pack evolution, rule IDs, exceptions, audit trail expectations, and policy test coverage.
- **Data Intake Steward** 🧰  
  Owns intake gates, boundary-artifact validity (contracts + STAC/DCAT/PROV), and “no mystery layers” enforcement.
- **Release Manager** 📦  
  Owns signed releases, SBOM/DBOM, attestations, promotion lane gating, and revocations.
- **Maintainers / Reviewers** 👀  
  Own branch protections, code/data review quality, and gate enforcement.
- **Deployment Operator (self-hosted installs)** 🧑‍💻  
  Owns runtime hardening, secrets management, monitoring, and incident containment actions.
- **Federation Steward (if enabled)** 🌐  
  Owns cross-instance allowlists, trust anchors, and rules for import/export of artifacts.

### 🧾 Governance ledger (recommended)

Maintain a lightweight, append-only **governance ledger** (human approvals + hashes) for:

- Sensitive data approvals (who/when/why)
- Exceptions to default precision restrictions
- Takedown/restriction events + remediations
- Publication approvals for “high impact” releases (major datasets, public layers, offline packs, federated artifacts)

Suggested location:

- `docs/governance/ledger/` *(append-only; one file per decision or per month)*

> [!TIP]
> Keep decisions in `docs/architecture/adr/` and approvals in `docs/governance/` so governance doesn’t live only in tribal memory.

---

## ⭐ Security invariants

KFM’s architecture uses **non-negotiable invariants** that double as security controls (intended to be enforced by CI) ✅🤖

1) 🧬 **Pipeline ordering is absolute**  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
No stage consumes artifacts that haven’t passed the previous stage’s **formal outputs + checks**.

2) 🧾 **Contract-first + evidence-triplet is mandatory**  
If something is accessible in the UI, exports, notebooks, or Focus Mode, it must be traceable to:
- ✅ a **contract artifact** *(schema/spec; versioned)*  
- ✅ the **evidence triplet**: **STAC + DCAT + PROV**  
No “mystery layers.” No “trust me bro.” 🚫

3) 🧊 **Raw zones are immutable (append-only)**  
`data/raw/<domain>/` is a preservation zone. Never rewrite raw inputs.  
Processing produces **new versions** (new digests + new PROV).

4) 🧪 **Deterministic, idempotent ETL**  
Same input + config ⇒ same output. Runs must be re-runnable safely.  
No partial publishes. No unreproducible outputs.

5) 🕸️ **Graph is derived, not hand-edited**  
The knowledge graph is built from validated catalogs/contracts/provenance.  
If the graph changes, the source artifacts must explain why (via PROV + PR).

6) 🔌 **API boundary rule**  
The UI (and notebooks) must **never** talk to Neo4j/PostGIS/object storage directly.  
All access goes through governed APIs (authZ, redaction, schema contracts). 🔐

7) 🌿 **Sovereignty + classification propagate**  
No output artifact may be **less restricted** than its inputs.  
Redaction/generalization is required to publish sensitive inputs safely.

8) 🚦 **Fail-closed promotion gates**  
Missing provenance, broken catalogs, unsafe links, secrets, or sensitive precision leakage → **block merge/publish**.

9) 🎬 **Evidence-first narrative (Story Nodes)**  
No unsourced narrative content.  
Facts must cite evidence; AI-assisted text must be labeled + provenance-linked.

10) 🤝 **Humans approve publishing**  
Automation may open PRs, run checks, and attach evidence — but merges/promotion remain governed and reviewable. 👀✅

11) 🌐 **Federation is opt-in and trust-anchored**  
Remote instances, registries, and catalogs are **untrusted by default**.  
Imports require **signature/attestation verification + policy compatibility checks**.

12) 🧯 **Kill switch is universal**  
A single, auditable mechanism can pause promotion/automation at any time — and must be honored by CI, agents, and release jobs.

> [!IMPORTANT]
> In KFM, **metadata is security-critical**. A broken license, unsafe remote href, missing PROV, or misclassification can become a supply-chain issue for downstream consumers.

---

## 🎯 Scope

KFM is a **geospatial + historical mapping + modeling platform** that typically includes:

- 🖥️ Web UI *(React/TypeScript; 2D MapLibre + optional 3D Cesium; story panels)*
- 📱 Mobile / PWA *(offline caching; field workflows; optional AR overlays)*
- 🔌 APIs/services *(FastAPI + REST/GraphQL; contract-first; policy-aware access control)*
- 🧰 Workers/pipelines *(ETL + analytics + publishing; deterministic jobs)*
- 🗄️ Spatial storage *(PostgreSQL/PostGIS)*
- 🕸️ Knowledge graph *(Neo4j; ontologies; citations)*
- 🔎 Search index *(optional; documents + story search)*
- 🪣 Object/artifact storage *(tiles, COGs, docs, artifacts, offline packs; optional OCI registry)*
- 🗂️ Catalog + provenance layer *(STAC/DCAT/PROV + contracts + manifests)*
- 🤖 AI layer *(Focus Mode; optional Watcher/Planner/Executor; PR-only execution)*
- 🌐 Federation (optional) *(cross-instance catalog + artifact sharing)*

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
  - “Geospatial DoS” payloads (massive geometries, decompression bombs, pathological tilesets) crashing pipelines/UI
  - Graph query complexity DoS (deep traversals, path explosion)
- Federation specific:
  - Importing untrusted catalogs/artifacts without verification
  - Signature/attestation bypass in OCI/artifact registry workflows
- Notebook / external client specific:
  - Token scope leakage, unsafe “bring-your-own-query” endpoints, export bypasses

### ✅ Offline packs / mobile / AR are in scope

If KFM supports **offline packs**, **PWA caching**, or **AR overlays**, vulnerabilities are in scope, including:
- Pack signature/attestation bypass
- Pack containing misclassified/restricted data
- Sensitive coordinate exposure via device caches
- Permission misuse (GPS/camera) or privacy leaks

---

## 🧩 Threat model

KFM’s threat surface includes more than code.

### 🎯 Assets we protect

- 🔐 Credentials (cloud keys, DB creds, service tokens, CI secrets)
- 🧾 Contract + catalog integrity (schemas + STAC/DCAT) + provenance integrity (PROV)
- 🗺️ Sensitive location data (protected/cultural sites, private infrastructure)
- 📦 Published artifacts (tiles/COGs/GeoJSON/GeoParquet, reports, model outputs, offline packs, OCI artifacts)
- 🎬 Narrative trust (Story Nodes/Focus Mode must be evidence-backed and labeled)
- 🤖 CI/CD supply chain (workflows/actions, artifact promotion, attestations)
- 🧑‍💻 User privacy (analytics/logs; accounts if enabled; moderation content)

### 👤 Likely threat actors

- Opportunistic attackers (common web vulns, exposed secrets, misconfig)
- Malicious data contributors (poisoning/tampering)
- Supply-chain attackers (dependencies/CI/actions)
- Data scrapers targeting sensitive coordinates or operational details
- Well-meaning contributors who accidentally leak restricted data

### 🧨 Common KFM-specific failure modes

- “It’s just metadata” mindset → unsafe STAC/DCAT hrefs, licensing gaps, missing provenance
- UI bypassing the API boundary → authZ/redaction failure
- Pipelines fetching remote assets without allowlists → SSRF + internal exposure
- Publishing exact sensitive coordinates (maps, story text, exports, offline caches)
- Weak integrity controls → silent tampering, untraceable outputs
- LLM prompt injection / retrieval poisoning → untrusted text trying to override governance
- Graph query/path explosion → DoS via overly deep traversals
- High-risk parsers (PDFs/images/3D assets) → decompression bombs / memory exhaustion
- Offline packs → restricted data “walks out the door” if misclassified or unsigned
- Federation → importing remote artifacts without signatures/policy compatibility
- Automation without kill-switch → autopublish drift during an incident

---

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries (v13-aligned) — at a glance</strong></summary>

```mermaid
flowchart LR
  EXT[🛰️ External Providers<br/>archives • APIs • feeds] -->|untrusted| INTAKE[🧰 Intake Gate<br/>contracts + checksums]
  INTAKE --> RAW[(🧊 data/raw/&lt;domain&gt;<br/>immutable)]
  RAW --> WORK[(🧪 data/work/&lt;domain&gt;<br/>scratch)]
  WORK --> PROC[(📦 data/processed/&lt;domain&gt;<br/>versioned outputs)]

  PROC --> STAC[🧾 STAC<br/>data/stac/collections + items]
  PROC --> DCAT[🗃️ DCAT<br/>data/catalog/dcat]
  PROC --> PROV[🧬 PROV<br/>data/prov/]
  STAC --> GRAPH[(🕸️ Knowledge Graph<br/>Neo4j • derived)]
  DCAT --> GRAPH
  PROV --> GRAPH

  GRAPH --> API[🔌 Governed API<br/>REST + GraphQL]
  PROC --> OBJ[(🪣 Object/Artifact Storage<br/>tiles • COGs • docs • packs)]
  OBJ --> API

  POLICY[(⚖️ Policy Engine<br/>OPA + rule packs)] --> API
  AUTH[(🔐 AuthN/AuthZ<br/>RBAC + ABAC)] --> API

  U[🌐 User / Client] -->|HTTPS| UI[🧑‍💻 Web UI<br/>React • MapLibre • (opt) Cesium]
  UI -->|governed calls| API

  NB[📓 Notebooks / External Clients] -->|token scoped| API

  API --> PACK[📦 Offline Pack Builder<br/>(signed + attested)]
  PACK --> U

  FED[🌐 Federated Instance<br/>remote STAC/DCAT/OCI] -->|untrusted| API
```

</details>

> [!IMPORTANT]
> Anything crossing a trust boundary must assume **untrusted input** until validated  
> (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses, PDFs, images, 3D assets, and federated metadata). 🚧

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
> Some datasets require **sovereignty and cultural protocols** beyond “Public vs Private.”  
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

### 🧩 Privacy-preserving release patterns (recommended)

When publishing sensitive-but-valuable data, consider:

- **Aggregation thresholds** (“don’t publish counts for groups smaller than _k_”)  
- **k-anonymity style constraints** for query outputs (k-minimums for any export result)  
- **Generalization** (grid cell or region-level) + **noise/jitter** (documented)  
- **Query auditing** for repeated “slicing” that could enable inference attacks

> [!TIP]
> In KFM, these patterns belong in **policy-as-code** so they’re enforceable at runtime (not just “best effort”).

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
- Avoid storing raw prompts or exports when not required; if stored, classify accordingly.

---

## 🧾 Contracts, catalogs & provenance requirements

KFM treats metadata and lineage as **security controls**, not “nice-to-have docs.”

### ✅ Boundary artifacts (publish bar)

Every dataset or evidence artifact that is promoted/published must have:

- 🧾 **Contract artifacts** *(schema/spec; versioned; validated)*  
  Examples: JSON Schema, OpenAPI, GraphQL SDL, UI layer registry config.
- 🧾 **STAC Collection + Item(s)** *(geospatial indexing + assets; includes KFM profile fields like dataset ID + classification)*
- 🗃️ **DCAT dataset entry** *(discovery + distributions + license; includes sovereignty/protocol metadata where applicable)*
- 🧬 **PROV lineage bundle** *(inputs → activities → outputs, with agents + parameters)*
- 🔎 **Cross-layer linkage** (bidirectional where possible):
  - Contracts ↔ STAC ↔ DCAT ↔ PROV
  - Graph references catalogs/contracts (no bulky raw data embedded)

> [!IMPORTANT]
> If contracts/catalogs/provenance don’t validate, **it does not ship**. 🚫📦

### 🗂️ Canonical v13 paths (enforced)

KFM v13 expects these locations as **canonical** (policy & CI should enforce):

- **Raw**: `data/raw/<domain>/` *(immutable)*  
- **Work**: `data/work/<domain>/` *(scratch / intermediate)*  
- **Processed**: `data/processed/<domain>/` *(versioned outputs)*  
- **STAC**: `data/stac/collections/` and `data/stac/items/`  
- **DCAT**: `data/catalog/dcat/` *(JSON-LD / dataset discovery)*  
- **PROV**: `data/prov/` *(lineage bundles)*

> [!TIP]
> Directory drift is a real security risk: it can hide unvalidated artifacts and bypass gates.

### 🧾 Dataset “data contracts” (recommended)

For dataset-level contracts (beyond STAC/DCAT), adopt one canonical layout and enforce it:

- ✅ Preferred: `schemas/contracts/datasets/<dataset_id>.json`  
- Alt (if you prefer docs-adjacent): `docs/data/<domain>/contracts/<dataset_id>.json`

A dataset contract should include, at minimum:

- `id` *(stable, unique)*
- `title`, `description`
- `license` + attribution fields
- `schema_version`
- spatial + temporal extent *(including CRS and reprojection notes)*
- provenance sources + processing summary
- **classification** + sensitive location policy fields
- **FAIR+CARE** fields *(recommended)*
- **sovereignty / cultural protocol** fields *(when applicable)*
- **approvals** *(where required: DUA/IRB/community review)*

### 🕸️ Knowledge graph integrity rules

- The graph is a **derived view** of governed artifacts.
- Prefer reproducible bulk import snapshots (e.g., `data/graph/csv/nodes.csv` and `data/graph/csv/edges.csv`).
- Use stable IDs, ontology alignment (e.g., CIDOC-CRM + GeoSPARQL + OWL-Time), and strict referential integrity checks.
- The graph must carry classification/protocol metadata so the API can enforce ABAC.

### 📦 Evidence artifacts (analysis/AI outputs)

Any analysis output or AI-generated dataset is treated as a **first-class dataset**:

- stored like a dataset (`data/processed/<domain>/...`)
- cataloged like a dataset (STAC/DCAT)
- traced like a dataset (PROV, including model/config + confidence)
- exposed only via governed APIs (never hard-coded into the UI)

---

## 🪪 Identity, access & auditability

KFM assumes **RBAC baseline** plus **ABAC enforcement** for classification and sovereignty tags.

### 🧑‍💼 RBAC baseline roles (recommended)

| Role | Typical capabilities |
|---|---|
| **Public Viewer** 🌍 | Read Public datasets; view published stories; export public views |
| **Contributor** 🧑‍🔧 | Propose data/stories via PR; run local validators; cannot publish |
| **Maintainer** 👀 | Review + merge; trigger promotion lanes; cannot bypass gates |
| **Data Steward** 🧾🌿 | Approve classification/protocol changes; authorize exceptions |
| **Admin** 🧨 | Manage users/secrets; emergency actions; incident containment |

### 🧷 ABAC requirements (classification-aware)

Every request returning data must enforce:

- dataset `classification`
- `sensitive_location_precision` / redaction tier
- `sovereignty` / `cultural_protocols` / protocol tags

ABAC applies to:

- exports
- offline pack builds
- Story Node renders
- Focus Mode evidence retrieval
- notebook tokens and external clients

### 🧾 Auditability expectations

- Privileged actions must be logged:
  - publish/promote
  - redact/remove
  - user/role changes
  - policy overrides
  - federation imports/exports
- **Policy version hash** should be recorded with decisions (especially denials/redactions).
- Logs must be access-controlled and retained per deployment needs.
- Prefer **structured logs** + **OpenTelemetry** for tracing across services.

---

## 🔏 Artifact integrity, reproducibility & release discipline

KFM treats both **code** and **data** as a supply chain.

### 🔐 Integrity signals (recommended baseline)

- **Checksums/digests** (SHA-256) for artifacts and large assets
- **Manifests** for dataset releases (files + hashes + contract/cat/prov IDs)
- **Immutability** for published artifacts (object storage versioning or content-addressed paths)
- **Reproducibility lane** for promotion (rebuild + compare hashes where feasible)
- **SBOM** for software releases + dependency review for PRs
- **DBOM** *(dataset bill of materials)* for data releases
- **Build provenance attestations** for release artifacts
- **Sigstore/Cosign signatures** for high-trust releases (code + data artifacts)

### 🧾 Dataset BOM (DBOM) concept (recommended)

Think “SBOM, but for datasets.” For a release, publish:

- contract ID + schema version
- STAC/DCAT identifiers
- PROV run record (inputs, activities, agents)
- asset list with digests
- license summary + attribution bundle
- classification + precision tier + sovereignty/protocol tags

Suggested location:

- `releases/data/<release_id>/dbom.json`
- `releases/data/<release_id>/checksums.sha256`

### 📦 Offline pack integrity (if supported)

Offline packs must be treated like releases:

- Packs must be **signed and attested** (build provenance + manifest)
- Packs must contain:
  - contract + catalogs + provenance for included datasets
  - a pack-level manifest listing hashes and classifications
  - explicit “what’s missing” if online system has more restricted data
- Packs must be **policy-filtered** (ABAC must be applied before inclusion)
- Packs must support **revocation/expiry** strategies (deployment-dependent)

> [!CAUTION]
> Offline packs can quietly become the highest-risk distribution channel if misclassified data slips in. Treat them as “export on steroids.” 🧯

---

## 🌐 Federation & cross-instance security

> [!NOTE]
> Federation is optional. If enabled, treat it like connecting to the public internet (because it is). 🌐⚠️

### ✅ Default stance

- **Remote instances are untrusted by default.**
- Federation requires:
  - allowlists (domains/instances/registries)
  - verification (signature/attestation)
  - policy compatibility (classification/sovereignty)

### 🔐 Import rules (recommended)

Before importing a remote dataset/artifact:

- Verify **signature/attestation** (Cosign/SLSA provenance where available).
- Validate **metadata** (STAC/DCAT/PROV schemas and KFM profiles).
- Enforce **classification propagation** (no “upgrade” of restriction).
- Enforce **link safety** (no unsafe remote hrefs; SSRF protections).
- Record a **federation PROV activity** (“Imported artifact X from instance Y”).

### 🧱 Cross-instance trust anchors

- Maintain a **trust store** of approved keys/certs:
  - `docs/governance/federation/trust-anchors/`
- Maintain an **instance allowlist**:
  - `docs/governance/federation/allowlist.yml`

### 🚫 Federation red lines

- ❌ No auto-fetching arbitrary URLs from remote STAC/DCAT entries.
- ❌ No importing datasets without license + attribution + classification.
- ❌ No cross-instance export of Restricted/Confidential data.

---

## 🤖 Focus Mode AI & automation security

Automation exists to reduce toil — **not** to bypass governance.

### 🧠 Focus Mode guardrails (non-negotiable)

- **Evidence-first retrieval**: Focus Mode relies on the graph + cataloged sources.
- **Citations required**: answers must cite contract/catalog/provenance-backed evidence.
- **Uncertainty over fabrication**: if evidence is missing, refuse or label uncertainty.
- **Policy-aware redaction**: classification + sensitive-location + sovereignty rules apply at response time.
- **Prompt injection defense**:
  - treat all retrieved text as untrusted
  - ignore instructions found inside documents/datasets
  - never follow “embedded” instructions from content

> [!IMPORTANT]
> Focus Mode must not become a “web-browsing bot” by accident.  
> If external web access is allowed in a deployment, it must be explicit, logged, allowlisted, and policy-gated.

### ✅ WPE model: Watcher → Planner → Executor (PR-only)

If we use agentic automation, it must follow:

- 👀 **Watcher**: detects drift/events (broken links, missing metadata, upstream changes)
- 🧠 **Planner**: produces a deterministic plan under policy constraints
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

- **Repo variable (preferred):** `KFM_KILL_SWITCH=true`
- **Optional file-based switch:** `📄 .kfm/kill-switch.yml`

Example pattern for publish jobs:

```yaml
- name: 🧯 Kill-switch check
  shell: bash
  run: |
    set -euo pipefail
    if [ "${KFM_KILL_SWITCH:-false}" = "true" ]; then
      echo "Kill-switch enabled via repo variable. Stopping publish lane."
      exit 1
    fi
    if [ -f ".kfm/kill-switch.yml" ]; then
      echo "Kill-switch file present (.kfm/kill-switch.yml). Stopping publish lane."
      exit 1
    fi
  env:
    KFM_KILL_SWITCH: ${{ vars.KFM_KILL_SWITCH }}
```

### 🧾 Model cards & evaluations (recommended)

Any AI model used in production-facing features should ship with:

- model card (purpose, training data sources, limitations)
- evaluation summary (including bias checks if relevant)
- provenance record tying the model artifact to its data + code + config

---

## ⚖️ Policy-as-code enforcement

KFM governance rules should be enforceable by machines. 🧠✅

### ✅ OPA/Rego + Conftest (recommended)

Policy-as-code should cover:

- contract required fields + versioning checks
- catalog validity and link safety
- provenance required on publish
- classification propagation
- sensitive location precision rules
- workflow least privilege (CI)
- action pinning and dependency hygiene
- federation allowlists + signature requirements
- AI rules (citations required; no unsourced claims; policy-aware redaction)

### 🏷️ Rule IDs (recommended style)

Use stable IDs so CI output is actionable:

- `KFM-PROV-001`: Processed data changed without matching PROV update
- `KFM-CAT-002`: STAC/DCAT link domain not in allowlist (SSRF prevention)
- `KFM-CLASS-001`: Output classification lower than input classification
- `KFM-STORY-001`: Story markdown contains unsafe HTML / injection risk
- `KFM-AI-001`: AI output missing citations / violates redaction policy
- `KFM-FED-001`: Federated import missing signature/attestation
- `KFM-PACK-001`: Offline pack includes Restricted/Confidential data

> [!TIP]
> Keep policies versioned in Git and treat the policy pack as a first-class release artifact.

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
- Set request size limits (GeoJSON uploads, style JSON, story media, 3D assets, etc.)

> [!CAUTION]
> WebGL + large assets can crash GPUs/browsers. Enforce size limits, progressive loading, and resource budgets.

### 🔌 API/service security

- AuthN + AuthZ for all sensitive routes
- RBAC/ABAC as needed (classification-aware)
- Rate limit expensive endpoints (exports, deep graph traversals, heavy spatial queries)
- Request/response schema validation (OpenAPI contracts)
- Audit logging for privileged actions (publish, promote, redact, federation import)
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
- Use parameterized queries everywhere
- Enable TLS for DB connections
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
- Avoid unsafe subprocess usage (`shell=True`) and hard-coded credentials

### 📓 Notebooks & external clients (if supported)

- Treat notebooks as **untrusted clients**:
  - use scoped tokens (least privilege)
  - enforce ABAC on every request
  - apply export throttles and aggregation thresholds
- Never embed long-lived secrets in notebooks.
- Prefer ephemeral environments and containerized kernels for shared notebooks.

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

- Contract validator gate (schemas/specs)
- STAC/DCAT quick gate (required fields, license/providers/extensions)
- Link-check critical `links[].href` (prevents “catalog poisoning” + SSRF)
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- Classification propagation checks
- Raster/vector safety checks (size limits, geometry validity, decompression defenses)
- Story Node lint:
  - markdown sanitization (deny raw HTML by default)
  - ensure referenced layer IDs exist
  - link safety checks
  - citations present for claims
- Federation gates (if enabled):
  - signature verification required for imports
  - remote allowlists enforced

### ⚖️ Governance gates via policy-as-code

Use **OPA/Rego** via **Conftest** (or equivalent) to enforce deny-by-default rules.

Example call (shape only; adapt to repo layout):

```bash
conftest test \
  --policy src/server/policy/rego \
  --all-namespaces \
  data/stac/ data/catalog/dcat/ data/prov/ data/processed/ .github/workflows/
```

---

## 🚨 Incident response expectations

KFM treats these as security incidents:

- secrets exposure
- sensitive location publication
- sovereignty/protocol violation (unauthorized access/disclosure)
- catalog poisoning / unsafe remote fetch behavior
- retrieval poisoning affecting Focus Mode trust
- integrity tampering of published artifacts/offline packs
- unauthorized access to DB/storage/graph
- compromised CI runners or supply-chain breakage
- federated import of unverified artifacts

### ✅ Minimum expectations (for maintainers)

- **Containment first**:
  - flip kill-switch
  - restrict access / revoke tokens
  - disable promotions (fail-closed)
  - pause offline pack distribution (if applicable)
  - pause federation imports/exports (if enabled)
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

## ✅ Supported versions

We prioritize fixes for actively developed code and active public distributions.

| Target | Supported for security fixes | Notes |
|---|---:|---|
| `main` branch | ✅ | Always supported |
| Latest tagged release | ✅ | Recommended for deployments |
| Latest data release / pack release | ✅ | If distributed publicly |
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
- **Affected component(s)** (UI/API/DB/pipelines/catalogs/CI/Focus Mode/offline packs/federation)
- **Safe proof of concept** *(non-destructive; no public exploit chains)*
- **Suggested fix** *(optional)*
- **Version/commit** tested
- **Environment** (OS/browser/runtime/container tags)

### 🧭 KFM-specific context that helps a lot

- Dataset IDs (e.g., `kfm.ks.<domain>.<layer>.<time>.vN`)
- STAC: `data/stac/**`
- DCAT: `data/catalog/dcat/**`
- PROV: `data/prov/**`
- Raw/Work/Processed: `data/{raw,work,processed}/<domain>/**`
- Graph snapshots: `data/graph/**` (if applicable)
- Contract artifacts: `schemas/**` (schemas/specs/SDL)
- Story Nodes: `docs/reports/story_nodes/**`
- Whether the issue leaks **exact coordinates** vs redacted/generalized outputs
- Whether the issue could be:
  - **catalog poisoning** (unsafe `links[].href`)
  - **retrieval poisoning** (graph nodes/docs altering Focus Mode behavior)
  - **offline pack leakage** (device storage/caches/pack manifest)
  - **federation import issue** (signature bypass / trust anchor mismatch)

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
- Paths/IDs (STAC/DCAT/PROV/contracts/schemas):
- Offline pack involved? (Y/N)
- Federation involved? (Y/N)
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

## 🗂️ Recommended repo security files

<details>
<summary><strong>📁 Suggested layout (v13-aligned)</strong></summary>

```text
📦 .github/
 ├─ 📄 SECURITY.md                 # ✅ this file (canonical)
 ├─ 📄 dependabot.yml
 ├─ 📄 CODEOWNERS
 └─ 📁 workflows/
    ├─ 📄 ci.yml
    ├─ 📄 codeql.yml
    ├─ 📄 policy-gate.yml
    ├─ 📄 contract-validate.yml
    ├─ 📄 catalog-qa.yml
    ├─ 📄 sbom.yml
    └─ 📄 attest.yml

📦 schemas/                         # contract artifacts (JSON Schema/OpenAPI/GraphQL SDL)
 └─ 📁 contracts/
    └─ 📁 datasets/                 # dataset-level data contracts (recommended)

📦 src/
 ├─ 📁 server/                      # governed API layer (FastAPI + GraphQL)
 ├─ 📁 ui/                          # React / MapLibre / (optional) Cesium
 ├─ 📁 pipelines/                   # ETL jobs (deterministic)
 └─ 📁 agents/                      # Watcher–Planner–Executor (PR-only)

📦 data/
 ├─ 📁 raw/
 │  └─ 📁 <domain>/
 ├─ 📁 work/
 │  └─ 📁 <domain>/
 ├─ 📁 processed/
 │  └─ 📁 <domain>/
 ├─ 📁 stac/
 │  ├─ 📁 collections/
 │  └─ 📁 items/
 ├─ 📁 catalog/
 │  └─ 📁 dcat/
 ├─ 📁 prov/
 └─ 📁 graph/
    └─ 📁 csv/

📦 docs/
 ├─ 📁 governance/
 ├─ 📁 architecture/
 │  └─ 📁 adr/
 ├─ 📁 standards/
 ├─ 📁 templates/
 ├─ 📁 security/
 ├─ 📁 data/
 │  └─ 📁 <domain>/
 │     └─ 📄 README.md             # domain runbook
 └─ 📁 reports/
    └─ 📁 story_nodes/             # Story Nodes (governed narratives)

📦 releases/
 ├─ 📁 software/
 └─ 📁 data/

📦 .kfm/
 └─ 📄 kill-switch.yml             # optional kill switch file
```

</details>

---

## 📚 Project reference library

> [!NOTE]
> These project files inform KFM’s defensive posture (governance, integrity, reproducibility, performance, privacy, and secure engineering).  
> They are **not** a request for offensive tooling contributions. 🚫🧨

### 🧭 Core KFM system documentation

- 📄 `MARKDOWN_GUIDE_v13.md.gdoc` *(canonical pipeline + contracts; v13 draft)*
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive Platform Overview and Roadmap.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf`
- 📄 `Kansas Frontier Matrix (KFM) – Comprehensive UI System Overview (Technical Architecture Guide).pdf`
- 📄 `📚 Kansas Frontier Matrix (KFM) – Expanded Technical & Design Guide.pdf`
- 📄 `Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf`

### 📦 Reference bundles (PDF portfolios; multi-book)

- 📚 `AI Concepts & more.pdf` *(digital humanism, accountability, AI governance framing)*
- 📚 `Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf` *(data management + CI/CD + integrity patterns)*
- 📚 `Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf` *(GIS ethics + WebGL/3D + archaeology sensitivity)*
- 📚 `Various programming langurages & resources 1.pdf` *(secure implementation references; defensive awareness)*
- 📚 `Mapping-Modeling-Python-Git-HTTP-CSS-Docker-GraphQL-Data Compression-Linux-Security.pdf` *(engineering/security references)*
- 📚 `Geographic Information-Security-Git-R coding-SciPy-MATLAB-ArcGIS-Apache Spark-Type Script-Web Applications.pdf` *(GIS + security + tooling references)*

### 🧪 Methods & reproducibility references

- 📄 `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf` *(reproducibility + peer review discipline)*
- 📄 `Data Mining Concepts & applictions.pdf` *(privacy-preserving release patterns and inference risk concepts)*
- 📄 `KFM- python-geospatial-analysis-cookbook-over-60-recipes...pdf` *(GIS pipeline patterns; keep security guardrails in mind)*

---

## 🧾 Appendix: Checklists & templates

### ✅ PR checklist (maintainers & contributors)

- [ ] No secrets committed (checked)
- [ ] Contract artifacts updated/added (if interfaces changed)
- [ ] STAC/DCAT/PROV updated/added (if publishable artifact changed)
- [ ] Graph snapshot regenerated (if relevant) and derived from governed artifacts
- [ ] Classification + sensitive precision reviewed (if location data present)
- [ ] Sovereignty/cultural protocol tags reviewed (if applicable)
- [ ] Link safety (no unsafe remote hrefs)
- [ ] Tests + validation gates passing
- [ ] Story content is sanitized + cites evidence (if Story Nodes changed)
- [ ] Focus Mode guardrails unchanged or reviewed (if AI layer touched)
- [ ] Offline pack changes reviewed + signed/attested (if applicable)
- [ ] Federation import/export rules satisfied (if applicable)

### ✅ “Ready to publish” checklist (promotion lane)

- [ ] All CI gates passing (contracts + catalogs + provenance + policy)
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
- Wire CI gates: CodeQL, dependency review, secret scanning, container scanning, contract validation, STAC/DCAT/PROV validation, policy-gate, story-lint.
- Keep OPA/Conftest policies tested (good/bad samples) and deny-by-default for promotion.
- Ensure kill switch is implemented and honored by all publish/sign workflows and agents.
- If federation is enabled: maintain trust anchors + allowlists; require Cosign verification on imports.
-->