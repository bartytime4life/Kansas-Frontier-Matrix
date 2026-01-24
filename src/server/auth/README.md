---
title: "🔐 Auth Module (Server)"
path: "src/server/auth/README.md"
status: "draft"
last_updated: "2026-01-24"
owners: ["KFM Core"]
tags: ["auth", "authorization", "jwt", "opa", "rego", "governance", "fair", "care", "provenance"]
---

# 🔐 Auth (Authentication + Authorization)

![Status](https://img.shields.io/badge/status-draft-yellow)
![Security](https://img.shields.io/badge/security-layered%20trust-blue)
![Policy-as-Code](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20Rego-4c1)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Access](https://img.shields.io/badge/access-RBAC%20%2B%20ABAC-orange)

> 🧭 **Mission:** keep KFM “open by default” for public exploration **while** providing serious access control for contribution workflows, restricted datasets, AI features, and provenance-safe exports.  
> This module implements the **security gatekeeper** for the server/API layer. :contentReference[oaicite:0]{index=0}

---

## ✨ Why this folder exists

The core docs explicitly anticipate an `auth/` area for **OAuth/token verification** and **role checks**.:contentReference[oaicite:1]{index=1}  
As KFM evolves toward multi-user collaboration (annotations, moderation, story drafting), the UI and back-end will require authenticated user accounts and permissions.:contentReference[oaicite:2]{index=2}

KFM also plans role-based permissions such as **public viewer**, **contributor**, and **admin**—with enforcement happening in the API (not just in the UI).:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

---

## 🧩 Scope & boundaries

### ✅ In scope
- **Authentication**
  - Bearer token verification (JWT / OIDC access tokens)
  - Service accounts for automation agents
- **Authorization**
  - RBAC (roles) + ABAC (attributes: dataset sensitivity, cultural protocols, purpose)
  - Policy-as-code enforcement via OPA/Rego
  - “Obligations” (redaction/obfuscation rules for responses)
- **Audit & provenance hooks**
  - Security/audit events (login, export, moderation actions) tied to provenance IDs
- **Secrets hygiene**
  - No secrets in repo, environment-based secret injection, CI secret scanning:contentReference[oaicite:5]{index=5}

### ❌ Out of scope (belongs elsewhere)
- UI login screens (front-end)
- Full identity provider hosting (use OIDC provider / SSO if possible)
- Database schemas for users (owned by `src/server/db/` or equivalent)
- Data pipeline governance checks (owned by policy pack tooling), though we **reuse** the same policy ideas at runtime:contentReference[oaicite:6]{index=6}

---

## 🏗️ Architectural position (server is the gatekeeper)

KFM’s front-end is designed to be decoupled and communicate through REST/GraphQL endpoints:contentReference[oaicite:7]{index=7}, and governance requires that clients **do not bypass the API to hit databases directly**.:contentReference[oaicite:8]{index=8}

That makes this module critical: **all access control happens here**, before any DB/file/graph reads.

---

## 📁 Suggested folder layout (contract)

> ⚠️ The exact filenames can differ; the point is the *responsibility split*.

```text
src/server/auth/
├─ 📘 README.md                       # 📘 This doc: auth architecture, flows, threat model notes, and how to test locally
├─ ⚙️ config/                         # Env parsing + defaults + validation (keep secrets out of git; fail-closed)
│  ├─ ⚙️📄 auth.config.(ts|py)         # Auth settings: issuer/audience, cookie/session options, dev toggles
│  └─ ⚖️📄 opa.config.(ts|py)          # OPA settings: bundle/version pinning, endpoints, timeouts, caching
├─ 🔑 providers/                      # Identity providers (OIDC, dev-local)
│  ├─ 🔑📄 oidc.(ts|py)                # OIDC provider integration (discovery, login redirect, claims mapping)
│  └─ 🧪🔑📄 dev_local.(ts|py)          # Dev-only provider (local users/roles; never enabled in prod)
├─ 🪪 tokens/                          # JWT verify/sign + refresh flows (token hygiene + key rotation support)
│  ├─ 🪪📄 jwt.(ts|py)                 # JWT helpers: verify, sign (if needed), decode claims, clock skew handling
│  └─ 🗝️🧊📄 jwks_cache.(ts|py)        # JWKS cache: fetch/refresh keys, pin issuer, retry/backoff, cache TTL
├─ ⚖️ policy/                          # Authorization rules + OPA bridge (central enforcement point)
│  ├─ ✅⚖️📄 authorize.(ts|py)          # authorize(...): policy decision entrypoint used by middleware/handlers
│  ├─ ⚖️🔌📄 opa_client.(ts|py)         # OPA client wrapper: decision calls, bundles, caching, error handling
│  └─ 🕵️🧹📄 obligations.(ts|py)        # Obligations: redaction/obfuscation actions required by policy decisions
├─ 🧱 middleware/                      # Request context injection (AuthN/AuthZ in the request pipeline)
│  ├─ 🧱🔐📄 authn_middleware.(ts|py)    # Authentication middleware: parse token/session → Principal + request context
│  └─ 🧱⚖️📄 authz_middleware.(ts|py)    # Authorization middleware: enforce decisions, apply obligations, map denials
├─ 🧾 audit/                           # Security events + provenance hooks (audit-safe; correlation IDs)
│  ├─ 🧾📄 audit_log.(ts|py)           # Audit logging: append-only events (login, denial, token errors, policy outcomes)
│  └─ 🔔📄 event_types.(ts|py)         # Event taxonomy: standardized audit event names + required fields
└─ 🧬 types/                           # Strong types for the auth boundary
   ├─ 🧑‍💼📄 principal.(ts|py)          # Principal model (subject id, display name, auth method, org/tenant)
   ├─ 🧑‍⚖️📄 roles.(ts|py)              # Roles/scopes mapping (RBAC/ABAC helpers)
   └─ 🎯📄 resources.(ts|py)           # Resource identifiers (dataset/layer/story ids) used in policy evaluation
```

This matches the platform’s emphasis on modular layers and explicit boundaries (UI ↔ API ↔ data stores).:contentReference[oaicite:9]{index=9}

---

## 👤 Identity model (Principal)

A **Principal** is the authenticated actor attached to each request.

Minimum recommended fields:

- `sub`: stable subject identifier
- `roles`: e.g. `public_viewer`, `contributor`, `admin`:contentReference[oaicite:10]{index=10}
- `groups`: optional group memberships (community, project team, reviewers)
- `attributes` (ABAC):
  - `purpose`: `"explore" | "research" | "moderation" | "ingestion"`
  - `affiliations`: partner orgs, tribal/community approvals (when relevant)
  - `risk`: derived (IP reputation, rate-limit tier, etc.)

> 🔎 Why ABAC? KFM needs to honor sensitivity + sovereignty constraints and avoid accidental leakage, including in derivative outputs.:contentReference[oaicite:11]{index=11}

---

## 🪪 Authentication approach

KFM documents describe typical API auth patterns using JWT tokens and role-based access at the API layer.:contentReference[oaicite:12]{index=12}

Recommended modes:

1. **OIDC / OAuth2 (preferred for production)**
   - Validate JWT access token via issuer JWKS
   - Use short TTL access + refresh token rotation
2. **Signed JWTs (self-issued, simple deployments)**
   - Server signs JWTs; clients present them as bearer tokens
3. **Service accounts (automation agents)**
   - For watcher/planner/executor style automation, issue scoped tokens and treat them as non-human principals:contentReference[oaicite:13]{index=13}

### Core invariants
- Always validate:
  - signature
  - `iss`, `aud`, `exp`, `nbf`
- Enforce least privilege via scopes/roles (contributors can upload but not publish without review; admins manage users):contentReference[oaicite:14]{index=14}
- Rate limit + sanitize inputs (API-wide):contentReference[oaicite:15]{index=15}

---

## ⚖️ Authorization approach (RBAC + ABAC + Policy-as-Code)

### RBAC (Roles)
Baseline permissions are role-driven:

| Role | Typical capabilities |
|---|---|
| 🌍 `anonymous` | read public datasets, public stories |
| 👀 `public_viewer` | same as anonymous + profile features |
| ✍️ `contributor` | propose uploads, create drafts, comment/annotate |
| 🧑‍⚖️ `reviewer` (optional) | approve/publish contributions |
| 🛠️ `admin` | manage users, roles, moderation, system config |

UI may hide actions (e.g., “upload”) unless the user is a contributor, but enforcement must be server-side in the API.:contentReference[oaicite:16]{index=16}

### ABAC (Attributes)
KFM data can be “restricted” (e.g., archaeological sites) with API enforcement that only certain roles can query it:contentReference[oaicite:17]{index=17}, and the UI may generalize or restrict sensitive layers unless permissions are granted.:contentReference[oaicite:18]{index=18}

Attributes commonly needed:
- dataset `sensitivity.classification` (public / internal / restricted / confidential)
- dataset `sovereignty` flags (CARE/Indigenous)
- request `purpose` (explore vs research vs export)
- output channel (tile vs raw export vs AI answer)

### Policy-as-Code (OPA / Rego)
KFM’s governance is formalized in a **Policy Pack** using OPA + Rego, with Conftest in CI, stored in-repo (e.g., `tools/validation/policy/*.rego`).:contentReference[oaicite:19]{index=19}

This module reuses that same philosophy at runtime:
- Evaluate policy for each protected action
- Fail closed by default for sensitive actions (deny unless allowed), matching governance stance:contentReference[oaicite:20]{index=20}

> 🧠 OPA can also be used at runtime to control what’s visible to different roles and to ensure no privacy constraints are violated.:contentReference[oaicite:21]{index=21}

---

## 🎛️ Authorization decisions include “obligations”

A simple allow/deny is not enough for KFM. Policies may require **transformations** like:
- coordinate rounding / geo-obfuscation for sensitive layers (example pattern: ~10km generalization):contentReference[oaicite:22]{index=22}
- field-level redaction (remove personally identifying info)
- result aggregation-only (no raw rows)
- export watermarking / credit requirements

This aligns with cultural protocol models (fine-grained access controls based on community rules).:contentReference[oaicite:23]{index=23}

### Example: OPA input/output contract

```json
{
  "input": {
    "principal": {
      "sub": "user_123",
      "roles": ["contributor"],
      "groups": ["ks_historians"]
    },
    "action": "dataset.read",
    "resource": {
      "type": "dataset",
      "id": "archaeology_sites",
      "classification": "restricted"
    },
    "context": {
      "purpose": "research",
      "channel": "map_tiles"
    }
  }
}
```

Expected OPA response shape:

```json
{
  "allow": true,
  "obligations": {
    "geo_obfuscation": { "method": "round", "meters": 10000 },
    "redact_fields": ["site_owner_name"],
    "include_credits": true
  }
}
```

---

## 🗺️ Data sensitivity rules (must-have)

KFM governance includes an explicit “carry forward the most restrictive classification” rule: outputs cannot be less restricted than inputs.:contentReference[oaicite:24]{index=24}

Implementation implications in this module:
- Authorization checks must consider **inputs + derived outputs**
- Export endpoints must always re-check classification and obligations
- Tile endpoints for restricted datasets should:
  - require auth
  - apply obfuscation obligations
  - enforce zoom-level constraints (blur/generalize at certain zooms):contentReference[oaicite:25]{index=25}

---

## 🧾 Audit logging & provenance hooks

KFM expects tokens and audit logs to provide traceability for actions like publishing, with logs capturing timestamps and actor identity.:contentReference[oaicite:26]{index=26}

Additionally, project ideas propose structured run manifests and hashing to create immutable identifiers for operations and to link them into provenance records.:contentReference[oaicite:27]{index=27}

### Audit events (recommended)
- `auth.login.success` / `auth.login.failure`
- `auth.token.issued` / `auth.token.revoked`
- `dataset.read` / `dataset.export`
- `dataset.upload.proposed` / `dataset.publish.approved`
- `story.draft.created` / `story.published`
- `ai.focus.query.executed` (with policy context)

> ✅ Store audit events with a stable `event_id` and attach to PROV/graph IDs whenever possible, to maintain “evidence-first” traceability.

---

## 🤖 AI features: permission-aware + prompt security

KFM’s architecture explicitly includes **prompt security** and “Prompt Gate” style policies to prevent prompt injection and accidental sensitive leakage.:contentReference[oaicite:28]{index=28}  
The AI system overview also calls out a dedicated prompt security subsystem for hardening Focus Mode against malicious inputs.:contentReference[oaicite:29]{index=29}

This module’s responsibilities for AI endpoints:
- authorize AI actions (`ai.focus.query`, `ai.story.suggest`, `ai.export.summary`)
- include dataset classification + user role context in policy input
- apply obligations (e.g., “only aggregated answers”, “must include citations”)

Governance policy rules also require that human-facing narrative content has citations and that AI-generated content is labeled; policy gates should fail if citations are missing or AI text is unmarked.:contentReference[oaicite:30]{index=30}

---

## 🔑 Secrets management (hard rule)

KFM’s repo policy is explicit: do not commit credentials/API keys; CI should scan and block leaks.:contentReference[oaicite:31]{index=31}  
Architecture docs also emphasize secrets are stored in secure vaults or environment configs and rotated/audited via policy.:contentReference[oaicite:32]{index=32}

### Requirements for this module
- Load keys (JWT signing keys, OIDC client secrets) only from:
  - secret manager
  - CI secret variables
  - runtime env vars
- Never log tokens, secrets, or sensitive claims

---

## 🧪 Local development

### Environment variables (recommended contract)

```bash
# Core identity
AUTH_MODE=oidc                # oidc | jwt_local | dev_local
AUTH_ISSUER=https://issuer.example
AUTH_AUDIENCE=kfm-api
AUTH_JWKS_URL=https://issuer.example/.well-known/jwks.json

# Local JWT mode (if used)
AUTH_JWT_PRIVATE_KEY_PEM=...
AUTH_JWT_PUBLIC_KEY_PEM=...
AUTH_ACCESS_TTL_SECONDS=900
AUTH_REFRESH_TTL_SECONDS=1209600

# OPA policy checks
OPA_URL=http://localhost:8181
OPA_QUERY=data.kfm.authz.allow
OPA_TIMEOUT_MS=100

# Audit
AUDIT_SINK=stdout             # stdout | db | queue
```

### Run OPA locally (example)
```bash
docker run --rm -p 8181:8181 openpolicyagent/opa:latest run --server
```

> 🧠 Keep runtime authz and CI policy pack aligned (same intent, shared semantics), even if the runtime package differs from the Conftest package layout.:contentReference[oaicite:33]{index=33}

---

## 🧯 Security checklist (PR review)

- [ ] Endpoint has explicit authn/authz middleware applied
- [ ] Authorization uses **resource classification** + role context:contentReference[oaicite:34]{index=34}
- [ ] Sensitive outputs obey “no less restricted than inputs”:contentReference[oaicite:35]{index=35}
- [ ] Tile/export endpoints implement obligations (obfuscation/redaction):contentReference[oaicite:36]{index=36}
- [ ] Rate limiting + input sanitation in place:contentReference[oaicite:37]{index=37}
- [ ] Secrets are not in code; CI secret scanning passes:contentReference[oaicite:38]{index=38}
- [ ] Audit events written for privileged operations:contentReference[oaicite:39]{index=39}

---

## 🗺️ Roadmap ideas (auth-specific)

- **Cultural protocol tags** (Mukurtu-style) as first-class ABAC attributes:contentReference[oaicite:40]{index=40}
- **Sensitivity-aware map rendering** obligations (blur/round/aggregate):contentReference[oaicite:41]{index=41}
- **Registry-backed private artifacts** (OCI artifacts) using registry auth + permission controls (for private data packs, models, etc.):contentReference[oaicite:42]{index=42}
- **Privacy-preserving query controls** to reduce inference risk in analytics workflows (audit + privacy-aware output constraints):contentReference[oaicite:43]{index=43}

---

## 📚 Project source docs used (internal)

> These are the project files that informed this README. Some are PDF portfolios that may require Adobe Reader to access embedded documents.:contentReference[oaicite:44]{index=44}:contentReference[oaicite:45]{index=45}:contentReference[oaicite:46]{index=46}:contentReference[oaicite:47]{index=47}

### Core KFM docs
- 🧱 **KFM – Comprehensive Technical Documentation** :contentReference[oaicite:48]{index=48} :contentReference[oaicite:49]{index=49} :contentReference[oaicite:50]{index=50}  
- 🧭 **KFM – Comprehensive Architecture, Features, and Design** :contentReference[oaicite:51]{index=51} :contentReference[oaicite:52]{index=52} :contentReference[oaicite:53]{index=53}  
- 🤖 **KFM – AI System Overview** :contentReference[oaicite:54]{index=54} :contentReference[oaicite:55]{index=55}  
- 🖥️ **KFM – Comprehensive UI System Overview** :contentReference[oaicite:56]{index=56} :contentReference[oaicite:57]{index=57} :contentReference[oaicite:58]{index=58}  
- 📥 **KFM – Data Intake (Technical & Design Guide)** :contentReference[oaicite:59]{index=59} :contentReference[oaicite:60]{index=60} :contentReference[oaicite:61]{index=61}  
- 🌟 **KFM – Latest Ideas & Future Proposals** :contentReference[oaicite:62]{index=62} :contentReference[oaicite:63]{index=63}  

### Innovation & extensions
- 💡 **Innovative Concepts to Evolve KFM** :contentReference[oaicite:64]{index=64} :contentReference[oaicite:65]{index=65}  
- 🧠 **Additional Project Ideas** :contentReference[oaicite:66]{index=66} :contentReference[oaicite:67]{index=67} :contentReference[oaicite:68]{index=68}  

### Reference libraries / portfolios
- 🧠 **AI Concepts & more (PDF portfolio)** :contentReference[oaicite:69]{index=69}  
- 🗺️ **Maps / GoogleMaps / VirtualWorlds / Geospatial WebGL (PDF portfolio)** :contentReference[oaicite:70]{index=70}  
- 🧰 **Various programming languages & resources (PDF portfolio)** :contentReference[oaicite:71]{index=71}  
- 🗃️ **Data Management theories & architectures (PDF portfolio)** :contentReference[oaicite:72]{index=72}  

### Extra extracted references (embedded/related)
- 🗺️ **Open-Source Geospatial Historical Mapping Hub Design** :contentReference[oaicite:73]{index=73}  
- 🕵️ **Data Mining Concepts & Applications (privacy/security context)** :contentReference[oaicite:74]{index=74}  
- 📝 **Comprehensive Markdown Guide (doc style reference)** :contentReference[oaicite:75]{index=75} :contentReference[oaicite:76]{index=76}

---
