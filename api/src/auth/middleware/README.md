# 🔐 Auth Middleware (API)

![JWT](https://img.shields.io/badge/Auth-JWT-blue)
![RBAC](https://img.shields.io/badge/Access-RBAC%20%2F%20ACL-purple)
![Audit](https://img.shields.io/badge/Security-Audit%20Logging-green)

> 🧠 **Goal:** one consistent place for request **authentication + authorization** guards so endpoints stay clean, predictable, and secure.

---

## 📁 Folder Location

## 🧭 Directory Layout (Auth Middleware)

```txt
📦 api/
└── 🧩 src/
    └── 🔐 auth/
        └── 🛡️ middleware/
            ├── 📘 README.md                   👈 you are here
            └── 🧰 (middleware modules...)     (auth guards, role checks, audit hooks)
```

> ✨ Tip: keep middleware modules **small + composable** (one concern per file), so routes can “stack” guards cleanly.

---

📎 Reference library: :contentReference[oaicite:0]{index=0}


---

## ✅ Ground Truth Requirements (from KFM docs)

These are **non-negotiable** expectations for how auth should behave across the backend:

- **JWT session auth:** login returns a **signed JWT** containing **user ID + roles**, and the token **expires** (example: ~1 hour). Sessions stay alive via a **refresh token mechanism**; refresh tokens are **long-lived**, stored securely, and only sent to the refresh endpoint. :contentReference[oaicite:0]{index=0}
- **Per-request verification:** the backend verifies the token **on each request**, including **signature + expiry** checks. :contentReference[oaicite:1]{index=1}
- **Role/resource authorization:** endpoints must check the user’s role **and** the requested resource (e.g., **ownership/organization assignment**). Unauthorized access should return **403 Forbidden**. :contentReference[oaicite:2]{index=2}
- **Operational access levels:** some endpoints are “admin only” / internal-only; the JWT claims include roles/levels and the **endpoint decorator or middleware** enforces them. :contentReference[oaicite:3]{index=3}
- **Systematic enforcement:** use your framework’s mechanisms (middleware/decorators/DI) so auth is **systematic**, not ad-hoc per endpoint. :contentReference[oaicite:4]{index=4}
- **All APIs require a valid token**, and write operations may require **CSRF** protection depending on how auth is transported (token-only vs cookies). :contentReference[oaicite:5]{index=5}
- **Audit logging:** log security-sensitive actions (login/logout/data changes/permission changes) with user ID + timestamp + details. :contentReference[oaicite:6]{index=6}
- **Secrets must not leak:** API keys/credentials (and by extension JWT signing secrets/keys) must be stored server-side, never exposed to clients, and never committed—use env vars or a vault/secret manager. :contentReference[oaicite:7]{index=7}

---

## 🎯 What Belongs in `auth/middleware/`

Think in layers (🧩 composable “guards”):

### 1) 🔎 Authentication (Who are you?)
- Extract token (typically `Authorization: Bearer <token>`).
- Verify token signature + expiry.
- Build an `AuthContext` and attach it to request context.
- Support **optional auth** (public routes that enhance response if logged in).

> KFM explicitly expects per-request verification and token expiry checks. :contentReference[oaicite:8]{index=8}

---

### 2) 🛂 Authorization (Are you allowed?)
Authorization should be **default-deny** and enforce:

- **Role checks** (RBAC): `admin`, `researcher`, `farmer/user`, etc. :contentReference[oaicite:9]{index=9}
- **Permission checks** (ACL mapping): role → permissions.
- **Ownership / org checks** for resources (fields, datasets, layers, etc.). :contentReference[oaicite:10]{index=10}

---

### 3) 🧯 Operational Access Levels (High-risk actions)
For dangerous endpoints (delete datasets, reload base data, “internal staff only” tooling), enforce an additional guard:

- `requireAccessLevel("admin")`
- `requireAccessLevel("data-engineer")` (example internal role) :contentReference[oaicite:11]{index=11}

---

### 4) 🧾 Audit + Observability Hooks
Provide reusable helpers to log:
- authentication events (success/failure),
- authorization denials,
- sensitive actions (mutations, permission changes).

KFM calls out audit logging as a key security measure. :contentReference[oaicite:12]{index=12}

---

### 5) 🔁 Service-to-Service Authentication (Internal calls)
If the API calls internal services (ML, ingestion, etc.), support one of:
- secure internal network + service boundaries, and/or
- a **service token** for internal auth. :contentReference[oaicite:13]{index=13}

---

## 🗺️ Request Lifecycle

```mermaid
flowchart TD
  A[Incoming request] --> B[Extract access token]
  B --> C{Token required?}
  C -- No --> H[Proceed (optional auth)]
  C -- Yes --> D[Verify JWT signature + expiry]
  D --> E{Valid?}
  E -- No --> U[401 Unauthorized]
  E -- Yes --> F[Attach AuthContext to request]
  F --> G[Authorization guard: role/permission/ownership/level]
  G --> I{Allowed?}
  I -- No --> X[403 Forbidden]
  I -- Yes --> J[Handler / Controller]
  J --> K[Audit log (when needed)]
```

---

## 🧾 Auth Context Contract (Recommended)

Keep the middleware boundary clean by emitting a consistent object (names may vary by framework):

```ts
// Example (TypeScript-ish) shape
export type AuthContext = {
  userId: string;           // from JWT "sub" or equivalent
  roles: string[];          // e.g., ["researcher"]
  accessLevels?: string[];  // operational access levels
  orgId?: string;           // if tenant/org scoping is used
  tokenId?: string;         // optional: jti
  issuedAt?: number;        // iat
  expiresAt?: number;       // exp
};
```

### ⚠️ Important rule
Even if the JWT contains role/level claims, **resource-level access** must still be verified against the system’s source of truth (DB/service), e.g., field ownership/org assignment. :contentReference[oaicite:14]{index=14}:contentReference[oaicite:15]{index=15}

---

## 🧱 Suggested Module Map (Recommended)

> This is a suggested layout; implement what the current codebase needs.

```txt
middleware/
├─ authenticate.(ts|js|py)        🔑 verify token, attach AuthContext
├─ optionalAuth.(ts|js|py)        🫥 attach AuthContext if present; never 401
├─ requireAuth.(ts|js|py)         🛑 enforce auth required
├─ requireRole.(ts|js|py)         👥 enforce RBAC role(s)
├─ requirePermission.(ts|js|py)   🧷 enforce ACL permission(s)
├─ requireAccessLevel.(ts|js|py)  🧨 internal/admin access levels
├─ requireOwnership.(ts|js|py)    🏡 resource ownership/org checks
├─ auditSecurity.(ts|js|py)       🧾 standardized audit events
└─ index.(ts|js|py)               📦 barrel exports
```

---

## 🧪 Usage Patterns

### 🟦 Express-style middleware (Node)
Express middleware typically uses the `function(req, res, next)` signature and calls `next()` to continue. :contentReference[oaicite:16]{index=16}

```ts
// Pseudocode
router.get(
  "/api/field/:id/timeseries",
  requireAuth(),
  requirePermission("field:read"),
  requireOwnership({ param: "id", resource: "field" }),
  controller.getFieldTimeseries
);

router.post(
  "/api/admin/reload-base-data",
  requireAuth(),
  requireAccessLevel("admin"),
  auditSecurity({ action: "RELOAD_BASE_DATA" }),
  controller.reloadBaseData
);
```

### 🟪 FastAPI-style dependencies (Python)
KFM explicitly notes using framework support like FastAPI dependency injection for auth to keep it systematic. :contentReference[oaicite:17]{index=17}

```py
# Pseudocode
@app.get("/api/field/{field_id}/timeseries")
def get_timeseries(
    field_id: str,
    auth=Depends(require_auth),
    _=Depends(require_permission("field:read")),
    __=Depends(require_ownership(resource="field", id_value=field_id)),
):
    ...
```

---

## 🚦 Status Codes (Consistency Matters)

- **401 Unauthorized** ✅  
  Use when the token is missing/invalid/expired for a protected endpoint.
- **403 Forbidden** ✅  
  Use when the token is valid, but the user lacks role/permission/ownership/access-level.  
  KFM explicitly calls out returning 403 when access checks fail. :contentReference[oaicite:18]{index=18}

---

## 🔐 Security Notes (Do / Don’t)

### ✅ Do
- Verify JWT **signature + expiry** on every protected request. :contentReference[oaicite:19]{index=19}
- Enforce **role + resource** checks (ownership/org assignment). :contentReference[oaicite:20]{index=20}
- Enforce **operational access levels** for “admin only” or internal endpoints. :contentReference[oaicite:21]{index=21}
- Audit log sensitive actions (and keep them queryable). :contentReference[oaicite:22]{index=22}
- Store secrets in env/vault, not source control, and never expose them to clients. :contentReference[oaicite:23]{index=23}

### 🚫 Don’t
- Don’t trust client-provided IDs/roles in request bodies/params (always rely on verified token + server-side checks).
- Don’t leak “why” a token failed in detail (avoid helping attackers).
- Don’t embed keys/secrets in code (including “temporary” ones). :contentReference[oaicite:24]{index=24}

---

## 🧷 Related Auth System Notes (Outside this folder, but tied to it)

These aren’t “middleware-only,” but the middleware should interoperate cleanly with them:

- Password hashing should use strong algorithms (bcrypt/Argon2). :contentReference[oaicite:25]{index=25}
- Brute-force defenses include rate-limiting login attempts and temporary lockouts after repeated failures. :contentReference[oaicite:26]{index=26}:contentReference[oaicite:27]{index=27}
- Optional MFA for sensitive/admin accounts. :contentReference[oaicite:28]{index=28}

---

## 📚 Sources

- 📘 **Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation** (security + backend auth/authorization)  
  :contentReference[oaicite:29]{index=29}  
- 📗 **Node.js Notes for Professionals** (Express middleware signature patterns)  
  :contentReference[oaicite:30]{index=30}

---

<p align="right"><a href="#-auth-middleware-api">⬆️ Back to top</a></p>

