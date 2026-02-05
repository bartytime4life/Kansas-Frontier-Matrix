# 🔐 Auth Hooks (`web/src/hooks/auth`)

<p>
  <kbd>React</kbd>
  <kbd>TypeScript</kbd>
  <kbd>RBAC</kbd>
  <kbd>OPA Policy Gates</kbd>
  <kbd>Fail-Closed</kbd>
  <kbd>CARE + FAIR</kbd>
</p>

> Centralized authentication state + request signing for the Kansas Frontier Matrix (KFM) web UI — designed to **support governance-first data access** (not bypass it).

---

## 🧭 Where Auth fits in KFM (why this exists)

KFM’s architecture routes **all client access** through a unified API layer (FastAPI with REST + GraphQL). This is intentional: by funneling requests through one place, KFM can enforce **authentication, authorization, and auditing** consistently (and avoid uncontrolled direct database access). [oai_citation:0‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

KFM also adopts a **“fail closed”** posture — if policy requirements aren’t satisfied, operations should be blocked by default. [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

This folder exists so the web app:
- ✅ Knows **who** the user is (identity)
- ✅ Knows **what the server says** the user can do (roles/claims for UX)
- ✅ Signs requests consistently (token/session + headers)
- ✅ Degrades safely when something is uncertain (fail closed)
- ✅ Keeps all auth plumbing **in one place** (easier to audit + test)

> **Important:** The UI may *reflect* permissions for UX (hide buttons, disable flows), but **server-side policy is the source of truth**. KFM uses RBAC + OPA policies to enforce real access control at runtime. [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ✅ Design goals

### 1) Respect the “single entry point” rule 🛡️
All data access must flow through the API layer so auth/authz/audit remain centralized. [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 2) Align with KFM’s RBAC + policy engine 🔑
KFM defines clear user roles and checks each request against both role and data sensitivity classification, enforced with OPA at runtime. [oai_citation:4‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 3) Protect sensitive and community-governed data 🪶
KFM flags certain sensitive data as restricted (e.g., some Indigenous site coordinates / sensitive personal information) and aims to follow FAIR+CARE principles in documentation and sharing. [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 4) Minimize token exposure 🧯
Storing API tokens in `localStorage` carries significant risks (notably XSS exposure) and offers no built-in guarantees for safe transfer; “token management is delicate.” [oai_citation:6‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

### 5) Make auth testable + observable 🧪
KFM emphasizes provenance and auditability at the system level; the frontend should help (consistent request paths, clean state machine, predictable failure modes). [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🚫 Non-goals (by design)

- ❌ **Authorization enforcement in the UI**  
  The API + OPA policy pack deny/allow (and may sanitize/mask) results at runtime. [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

- ❌ **Direct database access**  
  This is explicitly contrary to KFM’s governance model. [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

- ❌ **Long-lived secrets in browser storage**  
  Avoid `localStorage` for tokens in production-grade flows when possible. [oai_citation:10‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## 🗂️ Suggested folder layout (keep auth “boxed in”)

```text
web/src/hooks/auth/
  📄 README.md
  📄 index.ts                # single export surface ✅
  🧩 AuthProvider.tsx        # context provider
  🪝 useAuth.ts              # main auth hook (state machine)
  🪝 useAuthedFetch.ts       # fetch wrapper w/ refresh + retry
  🧾 types.ts                # AuthUser, AuthStatus, Role, etc.
  🧪 __tests__/              # unit tests for state + refresh logic
```

> Your actual filenames may differ — the goal is to keep **all auth entry points** discoverable and centralized.

---

## 🧩 Glossary (KFM-aligned)

- **Authentication** = verifying identity (“who are you?”). [oai_citation:11‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)
- **Authorization** = granting/denying access to resources based on permissions (“what can you do?”). [oai_citation:12‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)
- **RBAC** (role-based access control) = permissions scoped by role (e.g., viewer vs admin). [oai_citation:13‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- **OPA** (Open Policy Agent) = policy-as-code decision engine used to enforce rules on requests/outputs. [oai_citation:14‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- **Defense-in-depth** = layered security so no single control is the only line of defense. [oai_citation:15‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)

---

## 🧱 Public contract (what `useAuth()` should expose)

Even if the internal implementation changes, keep the *external* contract stable.

```ts
// types.ts (example contract)
export type AuthStatus = "loading" | "authenticated" | "unauthenticated" | "error";

export type KfmRole = "PUBLIC_VIEWER" | "CONTRIBUTOR" | "MAINTAINER" | "ADMIN";

export interface AuthUser {
  id: string;
  displayName?: string;
  email?: string;
  roles: KfmRole[];
  groups?: string[]; // optional: community/org/project groups
}

export interface UseAuthResult {
  status: AuthStatus;
  user: AuthUser | null;
  error?: { code: string; message: string };

  // actions
  signIn: () => Promise<void>;
  signOut: () => Promise<void>;

  // utilities
  hasRole: (role: KfmRole) => boolean;
  hasAnyRole: (...roles: KfmRole[]) => boolean;

  // request integration
  getAccessToken: () => Promise<string | null>;
}
```

### Why these roles?
KFM documentation describes roles such as **Public Viewer**, **Contributor**, **Maintainer**, **Admin**, with permissions scoped accordingly. [oai_citation:16‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

> Tip ✨: Keep role names in the UI normalized (e.g., enums), then map whatever the backend returns into your local `KfmRole` type.

---

## 🔁 Auth modes (pick one, but document it)

KFM’s API requests are “authenticated (via token or session)” and checked against role + data sensitivity classification. [oai_citation:17‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### Option A: Cookie-based session (recommended when possible 🍪)
- Browser automatically sends cookies
- Frontend uses `fetch(..., { credentials: "include" })`
- Safer because cookies can be configured `Secure` + `HttpOnly` (JS cannot read HttpOnly cookies) [oai_citation:18‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

**CSRF note:** If you use cookies for auth, protect state-changing requests with CSRF/XSRF tokens (a common approach is a server-issued token service). [oai_citation:19‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

### Option B: Bearer token (short-lived access token 🎟️)
- Frontend attaches `Authorization: Bearer <token>`
- **Avoid localStorage** for production-grade tokens when possible due to XSS exposure risk and lack of safe-transfer guarantees. [oai_citation:20‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

> If you must persist something client-side, treat it as non-sensitive and assume it’s readable by the browser; don’t store secrets in cookie values accessible to JS. [oai_citation:21‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

---

## 🌐 `authFetch()` / `useAuthedFetch()` (how API calls should work)

KFM expects auth + authorization + auditing to happen through the API layer, not ad-hoc in the UI. [oai_citation:22‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

A robust pattern:

1. Add auth (cookie credentials and/or bearer token)
2. Call API
3. If `401`, attempt a single refresh (dedupe concurrent refreshes)
4. Retry once
5. If still failing, fail closed → sign out / show login

```ts
// useAuthedFetch.ts (pseudocode)
let refreshInFlight: Promise<void> | null = null;

export async function authFetch(input: RequestInfo, init: RequestInit = {}) {
  // 1) attach credentials
  const mergedInit: RequestInit = {
    ...init,
    credentials: "include",
    headers: {
      ...(init.headers ?? {}),
      // "Authorization": `Bearer ${await getAccessToken()}` // if using bearer mode
    },
  };

  // 2) try request
  const res = await fetch(input, mergedInit);

  // 3) refresh on 401
  if (res.status === 401) {
    if (!refreshInFlight) {
      refreshInFlight = refreshSession().finally(() => (refreshInFlight = null));
    }
    await refreshInFlight;

    // 4) retry once
    return fetch(input, mergedInit);
  }

  return res;
}
```

> “Fail closed” UX suggestion: if refresh fails, return to `unauthenticated` state and do not continue making privileged calls. [oai_citation:23‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧾 Example: calling KFM’s versioned API endpoints

KFM’s REST endpoints are versioned (e.g., `/api/v1/...`). [oai_citation:24‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

Example dataset metadata call (from the docs): `GET /api/v1/datasets/{id}` returns dataset metadata and links to assets. [oai_citation:25‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

```ts
import { useAuth } from "./useAuth";
import { authFetch } from "./useAuthedFetch";

export function useDataset(id: string) {
  const { status } = useAuth();

  return async () => {
    if (status !== "authenticated") return null; // fail closed on the client

    const res = await authFetch(`/api/v1/datasets/${id}`);
    if (!res.ok) throw new Error(`Dataset fetch failed: ${res.status}`);
    return res.json();
  };
}
```

---

## 🧷 RBAC + policy gates (how to think about permissions)

### Roles are for UX; OPA is for enforcement ✅
KFM uses OPA policies to enforce access per request at runtime; e.g., “can user access dataset X?” and OPA can **deny** or **return a decision that triggers sanitization** (masking details like precise coordinates). [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

So in the UI:
- ✅ Use roles to show/hide controls (“Create story”, “Approve dataset”)
- ✅ Provide clearer error UX on `403`
- ❌ Never assume the UI is “enforcing security”

### Data sensitivity matters 🧊
KFM checks requests against the data’s sensitivity classification; certain high-sensitivity datasets may require Admin or special approvals (including privacy concerns or sacred Indigenous data). [oai_citation:27‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### CARE/FAIR alignment 🪶📚
KFM explicitly notes that sensitive data can be flagged with restricted access and that it aims to follow FAIR and CARE principles for documentation and sharing. [oai_citation:28‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
The CARE Principles are widely used to set minimum expectations for sharing Indigenous data while protecting rights/interests. [oai_citation:29‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)

> Practical takeaway: treat “restricted” as a *first-class state* in UI flows (copy, warnings, graceful denial paths).

---

## 🤖 Focus Mode + Auth (the AI assistant is not a bypass)

KFM’s “Focus Mode” flow is: UI sends the question to a backend endpoint (example given: `POST /ai/query`), the backend retrieves relevant context, calls a local LLM (via Ollama), attaches citations, then runs policy checks to block disallowed content (e.g., sensitive info). [oai_citation:30‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

That means:
- Focus Mode requests should be authenticated like any other API call
- The backend can check role + sensitivity before returning answers [oai_citation:31‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- The UI should be prepared for `403` or redacted responses (policy-driven)

---

## 🔐 Security checklist (frontend responsibilities)

### ✅ Prefer cookie/session + CSRF protections (when feasible)
- Cookies have attributes like `Secure` and `HttpOnly` (HttpOnly prevents JS access). [oai_citation:32‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)
- If auth is cookie-based, use CSRF/XSRF protection for state-changing requests (server-issued tokens are a common approach). [oai_citation:33‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

### ✅ Avoid `localStorage` tokens for real security
Storing tokens in `localStorage` exposes them to XSS and offers no inherent protection if requests accidentally go over insecure transport; careful token management matters. [oai_citation:34‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

### ✅ Treat anything readable by JS as non-secret
Cookie values accessible to the browser should not store sensitive data. [oai_citation:35‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)

### ✅ Embrace defense-in-depth
Use layers: access control (RBAC/MFA where applicable), request validation, and policy gates. Security should not depend on a single control. [oai_citation:36‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)

---

## 🧪 Testing notes (what to unit test)

Minimum tests that matter:

- `useAuth()` state machine:
  - `loading → authenticated`
  - `loading → unauthenticated`
  - `error` behavior + fail-closed defaults

- `authFetch()` behaviors:
  - adds `credentials: "include"`
  - retries once on `401`
  - dedupes refresh (only one refresh in flight)
  - signs out / resets state if refresh fails

- Role helpers:
  - `hasRole("ADMIN")` true/false
  - `hasAnyRole(...)` correctness

---

## 🧯 Troubleshooting

<details>
  <summary><strong>🔁 Infinite refresh loop (401 → refresh → 401 …)</strong></summary>

- Ensure refresh only retries **once** per request.
- Ensure refresh itself is not using the same interceptor logic (or it will recurse).
- Fail closed: if refresh fails, set `unauthenticated` and stop privileged polling. [oai_citation:37‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

</details>

<details>
  <summary><strong>🫥 UI says “not authorized” but server should allow</strong></summary>

- Treat UI permission checks as hints. The backend OPA policy pack is authoritative. [oai_citation:38‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- Fetch `/me` (or equivalent) again after role changes, and avoid caching role lists indefinitely.

</details>

---

## 📚 Source material (project files used)

- KFM architecture + governance (API as single entry point; auth/authz/audit) [oai_citation:39‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:40‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- KFM security posture (fail closed; RBAC roles; OPA runtime enforcement; no direct DB access) [oai_citation:41‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:42‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- OPA runtime decisioning + sanitization patterns (deny/mask) [oai_citation:43‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)  [oai_citation:44‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Sensitive data + FAIR/CARE alignment in KFM [oai_citation:45‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  [oai_citation:46‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)
- CARE Principles context for Indigenous Data Governance [oai_citation:47‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)  [oai_citation:48‡Indigenous Statistics.pdf](sediment://file_0000000033ec72308e1f791a79f61bfe)
- Client-side token storage cautions (localStorage risks; JWT/cookie strategies) [oai_citation:49‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  [oai_citation:50‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)
- Cookie security attributes (`Secure`, `HttpOnly`) [oai_citation:51‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)  [oai_citation:52‡Web Design.pdf](sediment://file_00000000d1987230b931eccca5ab6cda)
- Definitions of authentication/authorization + defense-in-depth framing [oai_citation:53‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)  [oai_citation:54‡Introduction to Digital Humanism.pdf](sediment://file_0000000090a071f5afd5c78c4383e488)