# 🛡️ Kansas Frontier Matrix (KFM) — Security Policy

<div align="left">

![Security Policy](https://img.shields.io/badge/security-policy-blue)
![Coordinated Disclosure](https://img.shields.io/badge/disclosure-coordinated-success)
![Private Reporting](https://img.shields.io/badge/reporting-private%20channel-important)
![PSA](https://img.shields.io/badge/PSA-no%20issues%2FPR%20comments-red)
![Supply Chain](https://img.shields.io/badge/supply--chain-SBOM%20%2B%20attestations-black)
![Data Integrity](https://img.shields.io/badge/data-integrity-PROV%20%2B%20checksums-purple)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-7c3aed)

</div>

> [!IMPORTANT]
> 🚨 **Do not report security vulnerabilities via public GitHub Issues, Discussions, or PR comments.**  
> Use **private vulnerability reporting** (preferred) or the alternative contact methods below.

> [!NOTE]
> KFM is a **geospatial + knowledge + modeling** system — security issues can live in **code**, **infrastructure**, **data catalogs**, **documents**, and **derived outputs** (models/Story Nodes/Focus Mode). Treat reports as potentially sensitive. 🧾🗺️

---

## ⚡ TL;DR (reporting in 60 seconds)

✅ **Preferred (private):** Repo **Security** tab → **Report a vulnerability**  
✅ Include: **impact**, **repro steps**, **affected component**, **commit/tag**, and (if relevant) **dataset IDs** (STAC/DCAT/PROV)

If you suspect **active exploitation**, put **“🚨 ACTIVE EXPLOITATION SUSPECTED”** in the title and report privately ASAP.

---

## 📌 Table of contents

- [🧾 Policy metadata](#-policy-metadata)
- [⭐ Security invariants](#-security-invariants)
- [🎯 Scope](#-scope)
- [🧩 Threat model (KFM-shaped)](#-threat-model-kfm-shaped)
- [🧱 Trust boundaries](#-trust-boundaries)
- [🔒 Data classification & sensitive location policy](#-data-classification--sensitive-location-policy)
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
| Last updated | **2026-01-09** |
| Review cycle | Quarterly 🔁 *(or after material security changes)* |
| KFM-MDP baseline | **v11.2.6** |
| Master Guide | **v13 (draft)** |
| Governance baseline | FAIR + CARE (data + people) |
| Applies to | This repo + official releases + supported deployments |

> [!TIP]
> GitHub recognizes `SECURITY.md` in the **repo root**, `.github/`, or `docs/`.  
> Keep **one canonical** file; mirrors are allowed, but **drift is a security risk**.

---

## ⭐ Security invariants

KFM’s architecture uses **non-negotiable invariants** that double as security controls (and are meant to be enforceable by CI) ✅🤖:

1) 🧬 **Pipeline ordering is absolute**  
**ETL → Catalogs (STAC/DCAT/PROV) → Graph → API → UI → Story Nodes → Focus Mode**  
Nothing bypasses earlier stages. If it’s visible, it’s cataloged and traceable. 🗂️🧾

2) 🔌 **API boundary rule**  
The UI must **never** talk to the graph DB or raw object storage directly.  
All access goes through governed APIs (authZ, redaction, schema contracts). 🔐

3) 🧾 **Provenance-first publishing**  
If it ships, it has:
- STAC/DCAT metadata
- PROV lineage
- (Recommended) checksums / stable IDs / content digests  
Metadata is **security-critical** (integrity + incident forensics). 🧬

4) ♻️ **Deterministic, idempotent ETL**  
Same input + config ⇒ same output. Pipelines must be re-runnable safely.  
No “mystery runs” or unreproducible outputs. 🧪

5) 🧭 **Sovereignty & classification propagate**  
No output artifact may be **less restricted** than its inputs.  
Redaction/generalization is required to publish sensitive inputs safely. ⚖️

6) 🚦 **Fail-closed validation gates**  
If provenance is missing, catalogs are broken, links are dead, secrets leak, or sensitive content appears → **block merge/publish**. 🧯

7) 🤝 **Humans approve publishing**  
Automation may open PRs, run checks, and attach evidence — but merges/promotion remain governed and reviewable. 👀✅

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
- 🧠 Trust in narratives (Story Nodes/Focus Mode must be evidence-backed and labeled)

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
> (files, JSON, GeoJSON, tilesets, STAC catalogs, external API responses, 3D assets). 🚧

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

## 🤖 Agent / automation security

KFM uses automation to *reduce human toil*, not to bypass governance.  
Agentic workflows (Watcher → Planner → Executor) are explicitly treated as **supply-chain sensitive**.

### ✅ Non-negotiables for automation (PR-only, evidence-backed)

- 🧯 **Kill switch exists** and is honored everywhere (CI + agents + promotion jobs)
- 🧾 **Idempotency key** logged in every artifact and PR body
- 🎲 **Deterministic seed + virtual clock** wired into planners and validators
- ⚖️ **Default-deny policy gates** (OPA/Rego via Conftest)
- 📦 **SBOM + provenance attestations** generated and attached (SLSA-ish)
- 🧪 **Reproducibility checks** compare rebuilt hashes
- 🔒 **Executor cannot merge** — branch protections remain the final gate

> [!NOTE]
> Automation may open/update PRs, but **humans merge** and publishing is governed.  
> This keeps the platform auditable and prevents “autopublish drift.” 👀✅

### 🛑 Kill switch pattern (recommended)

- Repo setting/secret: `KFM_KILL_SWITCH=true`
- Optional file-based switch: `.kfm/kill-switch.yml` (fail-closed)

Example CI guardrail:

```yaml
# example: reusable CI guardrails
- name: 🛑 Kill-switch check
  run: |
    if [ "${{ secrets.KFM_KILL_SWITCH }}" = "true" ]; then
      echo "Kill-switch enabled; stopping."
      exit 78
    fi
```

### 🔐 Minimal permissions for PR-opening automation

```yaml
# example: agents-executor.yml permissions
permissions:
  contents: read
  pull-requests: write
  id-token: write   # OIDC/Sigstore (attestation), NOT for merges
```

### 🧾 Required artifacts for any agent-driven change

Agent-driven changes should attach or reference:

- `plan.yml` (what/why; deterministic inputs)
- `diff.patch` (what changed)
- `reports/gates.json` (which gates ran, pass/fail)
- `prov/*.jsonld` (PROV bundle for the run)
- `attestations/*` (SBOM + build provenance)
- `telemetry/*.ndjson` *(recorded, not necessarily enforced during WIP)*

> [!IMPORTANT]
> If any gate fails, automation must **not** open/update a PR. Emit an event + link evidence instead. 🧯

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
  - File: `docs/security/pgp-public-key.asc`
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
- STAC path(s): `data/catalog/stac/...` *(or legacy `data/stac/...` if that’s the repo’s canonical)*
- DCAT path(s): `data/catalog/dcat/...`
- PROV path(s): `data/prov/...`
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

### 🧾 Catalog + provenance supply-chain security (STAC/DCAT/PROV as a control)
KFM treats **metadata + provenance** as security-critical:
- Provenance deters tampering and supports incident forensics
- Catalog validation prevents accidental publication of restricted data
- Checksums/versioning support reproducibility and rollback

**Before publishing any dataset or derived artifact:**
- STAC entry (when applicable)
- DCAT entry (when applicable)
- PROV lineage record (per run)
- (Recommended) checksums for large assets

> [!IMPORTANT]
> Any **derived/AI-generated** dataset is a first-class artifact with full provenance.

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
- Link-check critical `links[].href` in root/collections (prevent “catalog poisoning” paths)
- CRS + bounds validation (Kansas bounds where applicable)
- Provenance presence (PROV required before publish)
- “Classification propagation” checks (prevent public publish of restricted inputs)

### ⚖️ Governance gates (FAIR + CARE)
- License checks (no “unknown license” promoted without explicit approval)
- Sensitive location scans (deny-by-default for exact coordinates where disallowed)
- Sovereignty tags propagate from raw → processed → catalogs → API
- AI/narrative guardrails: **no unsourced claims** for public Story Nodes / Focus Mode outputs

### 🔏 Supply-chain controls (recommended for releases; optional for PRs)
- SBOM generation (SPDX)
- Signed commits for promotion branches
- Build provenance attestations (Sigstore/GitHub attestations)
- Reproducibility lane compares rebuilt hashes

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

### ✅ Minimum expectations (for maintainers)
- **Containment first**: stop automation (kill switch), restrict access, unpublish or revoke credentials
- **Preserve evidence**: keep logs, artifacts, and provenance records (don’t destroy audit trails)
- **Correct the catalog**: remove/disable affected STAC/DCAT entries and invalidate bad links
- **Patch & validate**: fix root cause, add regression tests, and rerun gates
- **Document**: write a short incident note (private if needed), plus public advisory if appropriate

> [!NOTE]
> Data takedowns (sensitive coordinates, restricted archives) should follow incident handling, even if no attacker is involved.

---

## 🗂️ Recommended repo security files

<details>
<summary><strong>📁 Suggested layout (v13-friendly)</strong></summary>

```text
📦 .github/
 ├─ 🛡️ SECURITY.md                # (optional mirror) policy copy
 ├─ 🧾 dependabot.yml
 ├─ 🧑‍⚖️ CODEOWNERS
 ├─ 🧪 workflows/
 │   ├─ 🔍 codeql.yml
 │   ├─ 🧾 dependency-review.yml
 │   ├─ 🔐 secret-scanning.yml     # docs + settings + optional checks
 │   ├─ 🧷 scorecard.yml           # OpenSSF (optional)
 │   ├─ ✅ ci.yml
 │   ├─ 🔎 catalog-qa.yml          # fast gate for STAC/DCAT fields + links
 │   └─ 🎬 story-lint.yml          # citations + sensitivity gates

📦 docs/
 ├─ 🔐 security/
 │   ├─ 🔑 pgp-public-key.asc
 │   ├─ 🧾 threat-model.md
 │   ├─ 📋 security-testing.md
 │   └─ 🧪 incident-response.md
 ├─ ❤️ governance/
 │   ├─ 🧭 data-classification.md
 │   ├─ 🗺️ sensitive-location-policy.md
 │   └─ ✅ review-gates.md

📦 tools/
 └─ ✅ validation/
     ├─ catalog_qa/
     └─ lanes/                     # CRS/bbox/schema/domain checks

📦 data/
 ├─ 📥 raw/
 ├─ 🧪 work/
 ├─ 🗄️ processed/
 ├─ 🗂️ catalog/
 │   ├─ stac/
 │   └─ dcat/
 └─ 🧬 prov/

📦 .kfm/
 └─ 🧯 kill-switch.yml             # optional file-based fail-closed switch
```
</details>

---

## 📚 Project reference library

> [!NOTE]
> These project files inform KFM’s defensive posture (threat modeling, governance, integrity, reproducibility).  
> They are **not** a request for offensive tooling contributions. 🚫🧨

<details>
<summary><strong>🏗️ KFM architecture, invariants, governance</strong></summary>

- `docs/specs/Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx`  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.docx](file-service://file-PaBDqECcJe7NbC8hvXNGDS)
- `docs/specs/MARKDOWN_GUIDE_v13.md.gdoc`  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) 
- `docs/specs/Latest Ideas.pdf`  [oai_citation:3‡Latest Ideas.pdf](file-service://file-Hc3LgRnWy8yxM8ME9TvpPg)  [oai_citation:4‡Latest Ideas.pdf](file-service://file-Hc3LgRnWy8yxM8ME9TvpPg)

</details>

<details>
<summary><strong>🔏 Supply-chain & promotion discipline (agents, attestation, policy gates)</strong></summary>

- `docs/specs/Latest Ideas.pdf` (Watcher/Planner/Executor, kill switch, idempotency, SBOM, Sigstore)  [oai_citation:5‡Latest Ideas.pdf](file-service://file-Hc3LgRnWy8yxM8ME9TvpPg)  [oai_citation:6‡Latest Ideas.pdf](file-service://file-Hc3LgRnWy8yxM8ME9TvpPg)  [oai_citation:7‡Latest Ideas.pdf](file-service://file-Hc3LgRnWy8yxM8ME9TvpPg)

</details>

<details>
<summary><strong>🗄️ Databases & scalable data systems</strong></summary>

- `docs/library/PostgreSQL Notes for Professionals - PostgreSQLNotesForProfessionals.pdf`
- `docs/library/Scalable Data Management for Future Hardware.pdf`  [oai_citation:8‡Scalable Data Management for Future Hardware.pdf](file-service://file-GZ8gMsQ8hxu7GWEVd3csNE)
- `docs/library/Data Spaces.pdf`

</details>

<details>
<summary><strong>🌐 Web UI, visualization & graphics</strong></summary>

- `docs/library/responsive-web-design-with-html5-and-css3.pdf`
- `docs/library/webgl-programming-guide-interactive-3d-graphics-programming-with-webgl.pdf`
- `docs/library/compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf`  [oai_citation:9‡compressed-image-file-formats-jpeg-png-gif-xbm-bmp.pdf](file-service://file-Y6V94sFtV6sy3w63LDy9fi)

</details>

<details>
<summary><strong>🌎 GIS, mapping & geoprocessing</strong></summary>

- `docs/library/python-geospatial-analysis-cookbook.pdf`
- `docs/library/making-maps-a-visual-guide-to-map-design-for-gis.pdf`
- `docs/library/Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf`  [oai_citation:10‡Mobile Mapping_ Space, Cartography and the Digital - 9789048535217.pdf](file-service://file-AkVmsLhdFzwie5Gco3zgYj)

</details>

<details>
<summary><strong>📊 Statistics, experiments & scientific computing integrity</strong></summary>

- `docs/library/Understanding Statistics & Experimental Design.pdf`
- `docs/library/regression-analysis-with-python.pdf`
- `docs/library/Regression analysis using Python - slides-linear-regression.pdf`  [oai_citation:11‡Regression analysis using Python - slides-linear-regression.pdf](file-service://file-Ekbky5FwpaPHfZC2ttv6xR)
- `docs/library/graphical-data-analysis-with-r.pdf`
- `docs/library/think-bayes-bayesian-statistics-in-python.pdf`  [oai_citation:12‡think-bayes-bayesian-statistics-in-python.pdf](file-service://file-LXwJApPMVhRZgyqLb9eg7c)
- `docs/library/Scientific Modeling and Simulation_ A Comprehensive NASA-Grade Guide.pdf`

</details>

<details>
<summary><strong>❤️ Ethics, autonomy & accountability</strong></summary>

- `docs/library/Introduction to Digital Humanism.pdf`
- `docs/library/Principles of Biological Autonomy - book_9780262381833.pdf`
- `docs/library/On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf`  [oai_citation:13‡On the path to AI Law’s prophecies and the conceptual foundations of the machine learning age.pdf](file-service://file-NtashtRjti9J1THyYXkhAv)

</details>

<details>
<summary><strong>🧰 Systems & concurrency</strong></summary>

- `docs/library/concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf`  [oai_citation:14‡concurrent-real-time-and-distributed-programming-in-java-threads-rtsj-and-rmi.pdf](file-service://file-Y45SvXbmLoZL1MNmrcyqz6)

</details>

<details>
<summary><strong>🛡️ Security references (defense only)</strong></summary>

- `docs/library/ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf`  [oai_citation:15‡ethical-hacking-and-countermeasures-secure-network-infrastructures.pdf](file-service://file-Q7EeqPb17SD9sV8Fb12LQX)
- `docs/library/Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf`  [oai_citation:16‡Gray Hat Python - Python Programming for Hackers and Reverse Engineers (2009).pdf](file-service://file-Mu6zixTqF9Lubf5QMjepRg)

> Used to inform defensive controls (threat modeling, incident response, testing strategy).  
> We do **not** accept contributions that add misuse-ready exploit instructions or weaponized tooling.

</details>

<details>
<summary><strong>📚 General programming shelf (bundles)</strong></summary>

- `docs/library/A programming Books.pdf`
- `docs/library/B-C programming Books.pdf`
- `docs/library/D-E programming Books.pdf`
- `docs/library/F-H programming Books.pdf`
- `docs/library/I-L programming Books.pdf`
- `docs/library/M-N programming Books.pdf`
- `docs/library/O-R programming Books.pdf`
- `docs/library/S-T programming Books.pdf`
- `docs/library/U-X programming Books.pdf`

</details>

---

<!--
Maintainers’ TODOs:
- Replace security@YOUR-DOMAIN.example with a real monitored inbox.
- Add PGP key at docs/security/pgp-public-key.asc and publish its fingerprint.
- Add incident-response runbook: containment, comms, logging, recovery, postmortem.
- Decide & document data classification rules + propagation enforcement.
- Wire CI gates: CodeQL, dependency review, secret scanning, container scanning, STAC/DCAT/PROV validation, story-lint.
- Add OPA/Conftest default-deny policies for promotion & sensitive location controls.
- Add kill switch: .kfm/kill-switch.yml + CI secret KFM_KILL_SWITCH.
-->