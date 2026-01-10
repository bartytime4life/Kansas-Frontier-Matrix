# 🛡️ Kansas Frontier Matrix (KFM) — Security & Governance Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)
![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![Policy as Code](https://img.shields.io/badge/policy-as%20code-OPA%20%2B%20Conftest-111827)
![Kill Switch](https://img.shields.io/badge/safety-kill--switch%20%2B%20fail--closed-red)
![Data Integrity](https://img.shields.io/badge/data-integrity-PROV%20%2B%20checksums-purple)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7c3aed)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling** system — security issues can live in **code**, **infrastructure**, **catalog metadata (STAC/DCAT)**, **provenance (PROV)**, **documents**, and **derived outputs** (models / Story Nodes / Focus Mode). Treat reports as potentially sensitive. 🧾🗺️

---

## ⚡ TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** + **STAC/DCAT/PROV paths**

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [⭐ Security invariants](#-security-invariants)
- [🎯 Scope](#-scope)
- [🧩 Threat model (KFM-shaped)](#-threat-model-kfm-shaped)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & sensitive location policy](#-data-classification--sensitive-location-policy)
- [🧾 Metadata & provenance requirements](#-metadata--provenance-requirements)
- [🤖 Agent / automation security](#-agent--automation-security)
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

---

## 🧾 Policy metadata

| Field | Value |
|---|---|
| Policy file | `SECURITY.md` *(canonical location: repo root **or** `.github/` — pick one and avoid drift)* |
| Status | Active ✅ |
| Last updated | **2026-01-10** |
| Review cycle | Quarterly 🔁 *(or after material security changes)* |
| KFM-MDP baseline | **v11.2.6** |
| Master Guide baseline | **v13 (draft)** |
| Governance baseline | FAIR + CARE (data + people) |
| Default posture | **Fail-closed** for promotion-critical gates 🚦 |
| Applies to | This repo + official releases + supported deployments |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> Keep **one canonical** file; mirrors are allowed, but **drift is a security risk**.

---

## ⭐ Security invariants

KFM’s architecture uses **non-negotiable invariants** that double as security controls (and are intended to be enforced by CI) ✅🤖:

1) 🧬 **Pipeline ordering is absolute**  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
No stage consumes artifacts that haven’t passed the previous stage’s **formal outputs + checks**.

2) 🔌 **API boundary rule**  
The UI must **never** talk to the graph DB or raw object storage directly.  
All access goes through governed APIs (authZ, redaction, schema contracts). 🔐

3) 🧾 **Boundary artifacts are security-critical**  
Before any dataset/evidence is considered “published,” it must have the **boundary artifacts**:
- 🧾 **STAC** (collections/items) for geospatial indexing
- 🗃️ **DCAT** for discovery/distribution
- 🧬 **PROV** for lineage (inputs → activities → outputs, with agents)
- 🧪 **Integrity signals** *(recommended)*: checksums/digests, stable IDs, manifests  
If it’s visible in downstream systems, it must be **cataloged + traceable**.

4) ♻️ **Deterministic, idempotent ETL**  
Same input + config ⇒ same output. Pipelines must be re-runnable safely.  
No “mystery runs” or unreproducible outputs. 🧪

5) 🧭 **Sovereignty & classification propagate**  
No output artifact may be **less restricted** than its inputs.  
Redaction/generalization is required to publish sensitive inputs safely. ⚖️

6) 🚦 **Fail-closed validation gates**  
If provenance is missing, catalogs are broken, links are unsafe, secrets leak, or sensitive content appears → **block merge/publish**. 🧯

7) 🎬 **Evidence-first narrative**  
No unsourced narrative content is allowed in Story Nodes or Focus Mode.  
Facts must cite evidence (cataloged sources), and AI-assisted text must be labeled and provenance-linked.

8) 🤝 **Humans approve publishing**  
Automation may open PRs, run checks, and attach evidence — but merges/promotion remain governed and reviewable. 👀✅

> [!IMPORTANT]
> In KFM, **metadata is security-critical**. A broken catalog link, missing license, or unsafe remote href can become a supply-chain issue for downstream consumers.

---

## 🎯 Scope

KFM is a **geospatial + historical mapping + modeling platform** that typically includes:

- 🖥️ Web UI (including WebGL/3D viewers)
- 🔌 APIs/services (e.g., FastAPI)
- 🧰 Workers/pipelines (ETL + analytics + publishing)
- 🗄️ Spatial storage (PostgreSQL/PostGIS)
- 🪣 Object storage (rasters/COGs, tiles, docs, artifacts)
- 🕸️ Knowledge graph (entities/events/citations)
- 🗂️ Catalog + provenance layer (STAC/DCAT/PROV)
- 🤖 Automation (GitHub Actions, agent workflows, promotion pipelines)

### ✅ In-scope vulnerability examples

- AuthN/authZ bypass (including IDOR), privilege escalation
- Injection (SQL/command), SSRF, stored/reflected XSS, CSRF with real impact
- Unsafe file upload, path traversal, deserialization issues, RCE
- Secrets exposure (tokens/keys), sensitive data leakage (**including precise coordinates**)
- Supply-chain risks introduced by this repo (dependencies, CI scripts, GitHub Actions)
- Geo-specific:
  - **Catalog poisoning** (malicious STAC/DCAT links/fields) causing unsafe fetches or consumer compromise
  - Integrity tampering of published assets (COGs/tiles/documents/model artifacts)
  - “Geospatial DoS” payloads (massive geometries, decompression bombs, pathological tilesets) that crash pipelines/UI

---

## 🧩 Threat model (KFM-shaped)

KFM’s threat surface includes more than code.

### 🎯 Assets we protect
- 🔐 Credentials (cloud keys, DB creds, service tokens, CI secrets)
- 🧾 Catalog integrity (STAC/DCAT) + provenance integrity (PROV)
- 🗺️ Sensitive location data (protected/cultural sites, private infrastructure)
- 📦 Published artifacts (tiles/COGs/GeoJSON/Parquet, reports, model outputs)
- 🎬 Narrative trust (Story Nodes/Focus Mode must be evidence-backed and labeled)
- 🤖 CI/CD supply chain (workflows/actions, artifact promotion, attestations)

### 👤 Likely threat actors
- Opportunistic attackers (common web vulns, exposed secrets, misconfig)
- Malicious data contributors (poisoning/tampering)
- Supply-chain attackers (dependencies/CI)
- Data scrapers targeting sensitive coordinates or operational details
- Well-meaning contributors who accidentally leak restricted data

### 🧨 Common KFM-specific failure modes
- “It’s just metadata” mindset → unsafe STAC links, licensing gaps, missing provenance
- UI directly contacting internal stores/graph → bypassing authZ/redaction
- Pipelines fetching remote assets without allowlists → SSRF + internal exposure
- Publishing exact sensitive coordinates in public layers/story content
- Weak artifact integrity controls → silent tampering, untraceable outputs
- Agent/automation without a kill-switch → autopublish drift under incident conditions

---

## 🧱 Trust boundaries

<details>
<summary><strong>🧩 KFM trust boundaries at a glance</strong></summary>

```mermaid
flowchart LR
  U[🌐 User / Client] -->|HTTPS| FE[🧑‍💻 Web UI<br/>(incl. WebGL/3D)]
  FE -->|governed calls| API[🔌 API / Services]
  API --> W[⚙️ Workers / Pipelines]
  API --> DB[(🗄️ Spatial DB<br/>PostgreSQL/PostGIS)]
  W --> OBJ[(🪣 Object Storage<br/>tiles • COGs • docs • artifacts)]
  W --> EXT[🛰️ External Providers<br/>GIS APIs • archives • feeds]
  API --> GRAPH[(🕸️ Knowledge Graph<br/>entities • events • citations)]
  API --> AUTH[(🔐 AuthN/AuthZ<br/>RBAC/ABAC as needed)]
```

</details>

> [!IMPORTANT]
> Anything crossing a trust boundary must assume **untrusted input** until validated  
> (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses, PDFs, and 3D assets). 🚧

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

> [!TIP]
> Good redaction strategies:
> - publish at **county/region** resolution instead of points  
> - snap to **grid cells** (H3/geohash) for public releases  
> - publish precise layers only via controlled access (private collections / signed URLs)

---

## 🧾 Metadata & provenance requirements

KFM treats metadata and lineage as **security controls**, not “nice-to-have docs.”

### ✅ Required boundary artifacts (publish bar)

Every dataset or evidence artifact that is promoted/published must have:

- 🧾 **STAC Collection + Item(s)** (or the project’s canonical STAC layout)
- 🗃️ **DCAT dataset entry** (title/description/license/keywords/distributions)
- 🧬 **PROV lineage bundle** (inputs → activities → outputs, with agents)
- 🔎 **Cross-layer linkage**:
  - STAC points to the assets
  - DCAT points to STAC and/or distributions
  - PROV links raw → work → processed and records run/config identifiers
  - Graph entries reference catalogs (not bulky raw data)

### 📦 Evidence artifacts (AI/analysis outputs)

Any analysis output or AI-generated dataset is treated as a **first-class dataset**:
- stored like a dataset
- cataloged like a dataset
- traced like a dataset
- exposed only via governed APIs (never hard-coded into the UI)

> [!IMPORTANT]
> If an AI-generated artifact could influence decisions, it must include uncertainty/limitations and remain provenance-linked.

---

## 🤖 Agent / automation security

Automation exists to reduce toil — **not** to bypass governance.

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

### 🧬 DevOps provenance (recommended)

KFM can map GitHub PR activity into PROV-like records:
- PR = Activity
- commits = Entities
- authors/reviewers/bots = Agents  
This supports auditability and ties changes to the same provenance universe as datasets.

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
- **Affected component(s)** (UI/API/DB/pipelines/catalogs/CI)
- **Safe proof of concept** *(non-destructive, no public exploit chains)*
- **Suggested fix** *(optional)*
- **Version/commit** tested
- **Environment** (OS/browser/runtime/container tags)

### 🧭 KFM-specific context that helps a lot
- Dataset IDs (e.g., `kfm.ks.<domain>.<layer>.<time>.vN`)
- STAC paths: `data/stac/**` *(or `data/catalog/stac/**` if that’s the repo canonical)*
- DCAT paths: `data/catalog/dcat/**`
- PROV paths: `data/prov/**`
- Whether the issue leaks **exact coordinates** vs redacted/generalized outputs
- Whether the issue could be **catalog poisoning** (unsafe `links[].href`, remote fetch behavior)

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
- STAC/DCAT paths or IDs:
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

**How to request a takedown / restriction change**
- Preferred: private vulnerability report (Security tab) labeled **“DATA TAKEDOWN / SENSITIVE DATA”**
- Include:
  - dataset ID(s)
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

### 🧾 Catalog + provenance supply-chain security (STAC/DCAT/PROV as control)
- Provenance deters tampering and supports incident forensics
- Catalog validation prevents accidental publication of restricted data
- Checksums/versioning support reproducibility and rollback

**Before publishing any dataset or derived artifact:**
- STAC entry (when applicable)
- DCAT entry (when applicable)
- PROV lineage record (per run)
- (Recommended) checksums/manifests for large assets

### 🛰️ External providers & live feeds (remote sensing, archives, APIs)
- Restrict API keys/service accounts by least privilege
- Separate “build” vs “publish” permissions
- Validate external inputs (bounds, schema, CRS, expected ranges)
- Treat external JSON/GeoJSON feeds as untrusted (SSRF + poisoning risks)
- Avoid embedding long-lived credentials in notebooks or exports

### 🌐 Web/UI security (including WebGL & 3D)
- Validate inputs on **server** (client validation is UX, not security)
- Encode outputs; avoid unsafe HTML injection
- Use secure cookies, CSRF protections where relevant, and a strict CSP
- Treat 3D assets (glTF/3D Tiles/etc.) as untrusted input
- Keep CORS least-privilege (avoid `*` with credentials)

### 🗄️ Database security (PostgreSQL/PostGIS)
- Separate read/write roles (and separate migration role if possible)
- Use parameterized queries everywhere (no string-built SQL)
- Encrypt backups; restrict access and audit restore paths
- Validate geometry (types, SRID, bounds) before insert
- Rate-limit expensive geospatial queries and exports

### ⚙️ Pipeline & worker safety (race conditions + resource safety)
- Make pipeline runs idempotent; avoid partial publishes
- Run decoders/parsers with guardrails (size limits, timeouts)
- Treat ZIPs, PDFs, images, and large geometries as hostile until validated
- Prefer atomic writes + staging directories + final “commit” step

### 🧠 ML/analytics integrity & safety
- Track dataset provenance, versions, checksums (poisoning defense)
- Separate train/eval/test; avoid leakage in artifacts
- Report uncertainty and limitations (avoid “false certainty”)
- Store model cards/experiment logs for any published ML output
- Be mindful of model inversion/membership inference for exposed models

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

### 🗂️ Catalog/data integrity checks (geo-specific)
- STAC/DCAT quick gate (required fields, license/providers/extensions)
- Link-check critical `links[].href` in root/collections (prevents “catalog poisoning”)
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- “Classification propagation” checks (prevent public publish of restricted inputs)

### ⚖️ Governance gates (FAIR + CARE) via **policy-as-code**
Use **OPA/Rego** policies via **Conftest** to enforce “default deny” rules for promotion.

✅ Recommended policy tool home:

```text
📁 tools/validation/policy/
├─ 📄 README.md
├─ 📁 rego/
│  ├─ 📁 common/
│  │  ├─ 📄 helpers.rego
│  │  ├─ 📄 license_allowlist.rego
│  │  └─ 📄 url_allowlist.rego
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
  data/ .github/workflows/ .github/actions/
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
- **Correct the catalog**:
  - remove/disable affected STAC/DCAT entries
  - invalidate unsafe external links
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
 │  ├─ 📄 catalog-qa.yml                 # STAC/DCAT quick gate + link safety
 │  ├─ 📄 policy-gate.yml                # Conftest/OPA gate for governed surfaces
 │  ├─ 📄 sbom.yml                        # SBOM generation (release lane)
 │  └─ 📄 attest.yml                      # provenance/build attestations (release lane)
 └─ 📁 actions/
    ├─ 📁 check-kill-switch/              # fail-closed stop button helper
    ├─ 📁 policy-gate/                    # conftest wrapper + bundles
    ├─ 📁 catalog-qa/                     # fast STAC/DCAT checks wrapper
    ├─ 📁 sbom/                           # SBOM helper
    └─ 📁 attest/                         # attestation helper

📦 tools/
 └─ 📁 validation/
    ├─ 📁 catalog_qa/
    └─ 📁 policy/                         # OPA policies + tests (see tree above)

📦 data/
 ├─ 📁 raw/
 ├─ 📁 work/
 ├─ 📁 processed/
 ├─ 📁 stac/                              # or 📁 data/catalog/stac/ (pick one canonical)
 ├─ 📁 catalog/
 │  └─ 📁 dcat/
 └─ 📁 prov/

📦 .kfm/
 └─ 📄 kill-switch.yml                    # optional file-based fail-closed switch
```
</details>

---

## 📚 Project reference library

> [!NOTE]
> These project files inform KFM’s defensive posture (threat modeling, governance, integrity, reproducibility).  
> They are **not** a request for offensive tooling contributions. 🚫🧨

- 📄 `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`
- 📄 `docs/specs/MARKDOWN_GUIDE_v13.md.gdoc`
- 📄 `docs/specs/Latest Ideas.pdf` *(agents, kill-switch, Detect→Validate→Promote, attestations, DevOps provenance)*
- 📁 `docs/library/` *(defensive references + data engineering + GIS + modeling discipline)*

<!--
Maintainers’ TODOs (keep this short and actionable):
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add PGP key at 📁 docs/security/📄 pgp-public-key.asc and publish its fingerprint.
- Add incident-response runbook: containment, comms, logging, recovery, postmortem.
- Wire CI gates: CodeQL, dependency review, secret scanning, container scanning, STAC/DCAT/PROV validation, policy-gate, story-lint.
- Keep OPA/Conftest policies tested (good/bad samples) and deny-by-default for promotion.
- Ensure kill switch is implemented and honored by all publish/sign workflows and agents.
-->
