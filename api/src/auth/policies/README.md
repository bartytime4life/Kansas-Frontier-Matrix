# 🔐 Auth Policies (Authorization)

![Security](https://img.shields.io/badge/security-authz-informational)
![Pattern](https://img.shields.io/badge/pattern-RBAC%20%2B%20resource%20checks-brightgreen)
![Sessions](https://img.shields.io/badge/sessions-JWT-blue)
![KFM](https://img.shields.io/badge/project-Kansas%20Frontier%20Matrix-6f42c1)

> **Source of truth for server-side authorization rules** ✅  
> Policies answer one question: **“Can this actor perform this action on this resource?”**

---

## 🧭 Table of contents

- <a href="#scope">📌 Scope</a>
- <a href="#architecture">🧱 Architecture fit (clean + testable)</a>
- <a href="#policy-flow">🧠 Policy flow</a>
- <a href="#roles">👥 Roles & access model</a>
- <a href="#operational">🧷 Operational access levels (admin-only / internal)</a>
- <a href="#conventions">🧩 Conventions (naming, decisions, permissions)</a>
- <a href="#examples">🧪 Examples (TypeScript-ish)</a>
- <a href="#testing">✅ Testing checklist</a>
- <a href="#security">🛡️ Security & privacy guardrails</a>
- <a href="#migration">🚚 Repo structure note (v13)</a>

---

<a name="scope"></a>
## 📌 Scope

### ✅ In-scope (belongs in `auth/policies/`)
- **RBAC / ACL rules** (role → permission checks)
- **Resource rules** (ownership, org membership, public/private flags)
- **Operational gates** (admin-only endpoints, staff-only tools)
- **Decision contracts** (`allow/deny` + optional reason codes)
- **Policy-focused unit tests** (matrix tests ✅)

### 🚫 Out-of-scope (keep elsewhere)
- Authentication flows: login, token issuance/refresh, MFA, password hashing
- HTTP wiring (middleware/decorators), request parsing, response formatting
- Direct DB queries (policies should be **pure**; pass the required data in)

> 🧠 Rule of thumb: **Policies should be runnable in a unit test without a web server or database.**

---

<a name="architecture"></a>
## 🧱 Architecture fit (clean + testable)

Policies should be **framework-agnostic** and accept **plain data** (IDs, roles, resource metadata), returning a **deterministic decision**.

This keeps authorization logic:
- **Portable** (usable from REST, GraphQL, jobs, CLI)
- **Auditable** (consistent deny reasons)
- **Testable** (fast policy matrix tests)
- **Harder to bypass** (server enforces rules; UI only reflects them)

---

<a name="policy-flow"></a>
## 🧠 Policy flow

```mermaid
flowchart TD
  A[Client Request] -->|Authorization: Bearer &lt;JWT&gt;| B[API Gateway / Router]
  B --> C[AuthN: verify token + build actor context]
  C --> D[AuthZ: call policy(action, actor, resource)]
  D -->|allow ✅| E[Controller / Use Case]
  D -->|deny ❌| F[403 Forbidden (or equivalent)]
  E --> G[Data access is filtered + redacted as needed]
```

### Key expectation
Even if the UI hides a button, the **API must still deny** unauthorized access.

---

<a name="roles"></a>
## 👥 Roles & access model (KFM default)

KFM’s docs describe these baseline roles (custom roles may exist per deployment):

| Role | Typical scope | Examples |
|------|---------------|----------|
| 👤 Farmer / User | Own fields + public datasets | View field timelines for owned fields, run permitted analyses |
| 🧑‍🔬 Researcher | Broad read access (but restricted from private user info) | Explore datasets across many fields, export aggregate layers |
| 🛠️ Admin | Full control | Manage users, system settings, global data edits |

> 🧷 Policies should support **resource-based constraints** even for broad roles (e.g., “private field details” vs “public field data”).

---

<a name="operational"></a>
## 🧷 Operational access levels (admin-only / internal)

Some actions are sensitive enough to require **explicit operational gates**, even if a user is authenticated:
- “admin only” endpoints (dangerous mutations, deletes, reload base data)
- internal tools (raw uploads, rebuild indexes, migration helpers)
- service-to-service calls (ML service, pipeline workers, etc.)

> ✅ Treat operational gates as first-class policy checks (not scattered `if (isAdmin)` conditionals).

---

<a name="conventions"></a>
## 🧩 Conventions (naming, decisions, permissions)

### 📛 File naming
Keep policies discoverable and consistent:

```
📁 api/src/auth/policies/
├── 📄 README.md
├── 📄 index.ts                 # barrel exports
├── 📄 field.policy.ts          # field resource rules
├── 📄 dataset.policy.ts        # dataset/catalog rules
├── 📄 user.policy.ts           # user profile visibility rules
└── 📄 admin.policy.ts          # admin/internal operations
```

### 🔑 Permission naming
Use a stable, searchable permission string:

- `field:read`
- `field:timeseries:read`
- `field:write`
- `dataset:read`
- `dataset:export`
- `admin:users:manage`
- `ops:raw_upload`

> 🧠 Tip: Keep permission strings **version-stable** (changing them is a contract change).

### ✅ Policy decision contract
Prefer a small decision object (easy to test + log):

```ts
export type PolicyDecision =
  | { allow: true }
  | { allow: false; reason: string; code?: "FORBIDDEN" | "NOT_OWNER" | "REDACTED" };

export const ALLOW: PolicyDecision = { allow: true };
export const deny = (reason: string, code?: PolicyDecision["code"]): PolicyDecision => ({
  allow: false,
  reason,
  code,
});
```

### 🧼 Purity rules
Policies should:
- be **deterministic** (same inputs → same outputs)
- avoid side effects (no logging inside policies; return reasons instead)
- avoid deep framework types (no `req`, no `res`, no ORM instances)

---

<a name="examples"></a>
## 🧪 Examples (TypeScript-ish)

> These are examples/pseudocode. Adapt to your framework (Express/Nest/Fastify/etc.) and your domain models.

### 1) Actor + resource context
```ts
export type Role = "user" | "researcher" | "admin" | "data_engineer";

export interface Actor {
  id: string;
  roles: Role[];
  orgId?: string;
  // Optional: operational level flags, feature flags, etc.
  ops?: {
    isStaff?: boolean;
    level?: "user" | "staff" | "admin";
  };
}

export interface FieldResource {
  id: string;
  ownerUserId?: string;
  ownerOrgId?: string;
  isPublic?: boolean;
}
```

### 2) Field read policy (ownership + public)
```ts
import { ALLOW, deny, PolicyDecision } from "./_shared";

export function canReadField(actor: Actor, field: FieldResource): PolicyDecision {
  if (actor.roles.includes("admin")) return ALLOW;

  // Public data is readable by authenticated users (adjust if you support anon reads)
  if (field.isPublic) return ALLOW;

  // Ownership / org assignment checks
  if (field.ownerUserId && field.ownerUserId === actor.id) return ALLOW;
  if (field.ownerOrgId && actor.orgId && field.ownerOrgId === actor.orgId) return ALLOW;

  if (actor.roles.includes("researcher")) {
    // Researcher access can be broad, but still respect privacy and deployment rules.
    // If researchers *should* see private fields, allow here. If not, deny.
    return deny("Researcher access to private fields is disabled in this deployment", "FORBIDDEN");
  }

  return deny("Not owner and not public", "NOT_OWNER");
}
```

### 3) Admin-only operation policy (operational gate)
```ts
export function canRunDangerousOperation(actor: Actor): PolicyDecision {
  if (actor.roles.includes("admin")) return ALLOW;
  return deny("Admin role required", "FORBIDDEN");
}
```

### 4) Wiring into routes (conceptual)
```ts
// router.get("/api/field/:id/timeseries",
//   requireAuth(),
//   authorize("field:timeseries:read", async ({ actor, params }) => {
//     const field = await fieldRepo.getById(params.id);
//     return canReadField(actor, field);
//   }),
//   handler
// );
```

---

<a name="testing"></a>
## ✅ Testing checklist

A good policy PR includes:

- [ ] Unit tests for each new policy rule
- [ ] “Matrix” tests (roles × actions × resource states)
- [ ] Edge cases:
  - [ ] public vs private resources
  - [ ] owner vs non-owner
  - [ ] org-assigned vs not assigned
  - [ ] operational level required
- [ ] Deny reasons are stable + meaningful (good for audit trails)

> 🧪 Pro tip: snapshot the role/action matrix so regressions show up as clear diffs.

---

<a name="security"></a>
## 🛡️ Security & privacy guardrails

### 🔒 Prevent “UI-only security”
- Never rely on UI controls for access control.
- Always enforce policies **server-side**.

### 🕵️ Prevent data leakage
- List/search endpoints must **filter at query time** (don’t fetch-all then filter in memory).
- Consider response-level redaction (e.g., hide private metadata fields) in addition to allow/deny.

### 🧾 Audit-friendly decisions
- Prefer deny reasons/codes that can be logged upstream (middleware/controller).
- Keep the policy layer pure; do logging in the enforcement layer.

### 🧯 Fail closed
- If required context is missing (no actor, no resource metadata), deny by default.

---

<a name="migration"></a>
## 🚚 Repo structure note (v13)

KFM v13 guidance centralizes server-side API code under `src/server/` (legacy `src/api/` may be merged).  
If your branch follows the v13 structure, mirror/move this folder accordingly:

- From: `api/src/auth/policies/`
- To: `src/server/auth/policies/` (or your API module’s canonical home)

---

🧠 **If you’re adding a new endpoint:**  
Treat permissions/policy behavior as part of the API’s “contract.” Update any relevant API contract docs and tests alongside the policy.

