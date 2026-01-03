# 🔐 Auth Utils

![Security](https://img.shields.io/badge/Security-Auth_Utils-success)
![JWT](https://img.shields.io/badge/Auth-JWT-blue)
![RBAC](https://img.shields.io/badge/Auth-RBAC-important)
![MFA](https://img.shields.io/badge/Auth-MFA_optional-informational)

> 📍 **Location:** `api/src/auth/utils/`  
> Small, reusable auth/security helper functions used across the API auth stack (tokens, passwords, RBAC, MFA, audit helpers). Keep these utilities **framework-agnostic**, **unit-testable**, and **safe-by-default**. ✅[^kfm-arch]

---

## 🧭 What belongs here vs elsewhere

✅ **Belongs here (utils)**  
- Token helpers: `signJwt()`, `verifyJwt()`, claim parsing, expiry checks  
- Password helpers: hash/verify (bcrypt/Argon2), strength checks  
- Refresh/reset token helpers (generate/validate/rotate *logic*)  
- RBAC/ACL helpers (role → permissions, “admin-only” guard predicates)  
- MFA helpers (OTP validation, challenge formatting)  
- Audit-event builders (shape/metadata standardization)

❌ **Does NOT belong here**  
- DB calls (storing refresh token hashes, lockout counters, etc.)  
- HTTP request/response objects (Express/Nest/Fastify specifics)  
- Email/SMS sending (belongs in notifier/service layer)  
- Rate-limit storage (Redis/in-memory) — **policy helpers are ok**

> 💡 Why: KFM is designed with layered separation—inner logic stays decoupled from outer frameworks. Utilities should remain “import-safe” and side-effect-light.[^kfm-arch-utils]

---

## 📦 Folder map

```text
api/                           🧬 API boundary (KFM backend surface)
└── src/                       🧠 Runtime source (app code)
    └── auth/                  🔐 AuthN/AuthZ core
        └── utils/             🧰 Security helper kit (pure + reusable)
            ├── README.md      📘 you are here ✅
            └── *.ts/*.js      🧩 jwt | rbac | mfa | audit | crypto helpers
```

<details>
<summary>✨ Suggested module split (rename to match actual code)</summary>

```text
jwt.ts            # access/service token helpers (sign/verify, claims)
refreshToken.ts   # refresh token generation/rotation helpers
password.ts       # hash/verify + strength checks
resetToken.ts     # one-time password reset token helpers
rbac.ts           # roles/permissions + guard predicates
mfa.ts            # optional OTP helpers
audit.ts          # audit event builders
index.ts          # barrel exports
```

</details>

---

## 🔑 Auth flows supported

### 1) Access tokens (JWT)

KFM uses **token-based authentication** with **JWTs**: after login, clients include `Authorization: Bearer <token>` and the backend verifies **signature + expiry** on every request.[^kfm-auth-backend]

Recommended traits:
- **Short-lived** access tokens (KFM example: ~1 hour)[^kfm-user-auth]  
- Claims include **user id** + **roles** (and optionally operational access levels)[^kfm-auth-backend]

Example claim shape (TypeScript-ish):

```ts
export type AccessTokenClaims = {
  sub: string;              // user id
  roles: Array<'farmer' | 'researcher' | 'admin' | string>;
  accessLevels?: string[];  // optional "operational access levels"
  iat: number;
  exp: number;
};
```

---

### 2) Refresh tokens

KFM keeps sessions alive via a **refresh token mechanism**: refresh tokens are **long-lived**, stored securely, and only sent to a dedicated refresh endpoint.[^kfm-user-auth]

🔐 Treat refresh tokens like credentials:
- store securely (prefer httpOnly cookie or similarly protected storage)
- never log them
- consider hashing at rest in DB (**DB logic lives outside utils**)

---

### 3) Password security + resets

KFM password security includes:
- Strong password hashing (bcrypt or Argon2)[^kfm-user-auth]
- Password reset via **one-time token** sent to email and required to set a new password[^kfm-user-auth]

---

### 4) Brute-force protection (lockout / rate limit)

KFM uses **rate-limiting** and **temporary lockouts** after repeated failures.[^kfm-auth-backend][^kfm-user-auth]

Utilities can support this by:
- computing lockout windows  
- normalizing usernames/emails  
- generating consistent failure responses (avoid user enumeration)

---

### 5) MFA (optional)

For sensitive/admin accounts, KFM supports **optional MFA** (OTP via authenticator app or email).[^kfm-user-auth]

---

### 6) Authorization (RBAC + operational access levels)

KFM authorization uses roles/privileges and ownership checks:
- Roles like **farmer / researcher / admin**[^kfm-user-auth]  
- Endpoints validate role + resource ownership (deny with 403 when unauthorized)[^kfm-auth-backend]  
- “Admin only” endpoints are enforced via **operational access levels**, checked through middleware/decorators/DI (framework-specific)[^kfm-auth-backend][^kfm-user-auth]

---

## 🧰 Usage patterns

> These examples are framework-agnostic by design. Adapt to Express/Nest/Fastify/etc.

### ✅ Verify access token + attach user context

```ts
import { verifyAccessToken } from './jwt';

export function authMiddleware(req, res, next) {
  const header = req.headers['authorization'] ?? '';
  const token = header.startsWith('Bearer ') ? header.slice(7) : null;

  if (!token) return res.status(401).json({ error: 'Missing token' });

  const { ok, claims } = verifyAccessToken(token);
  if (!ok) return res.status(401).json({ error: 'Invalid token' });

  req.user = {
    id: claims.sub,
    roles: claims.roles,
    accessLevels: claims.accessLevels ?? [],
  };

  return next();
}
```

---

### ✅ Role/permission guard

```ts
import { canAccessField } from './rbac';

export function requireFieldAccess(req, res, next) {
  const user = req.user;
  const fieldId = req.params.fieldId;

  if (!canAccessField(user, fieldId)) {
    return res.status(403).json({ error: 'Forbidden' });
  }

  return next();
}
```

> KFM examples explicitly mention checking field ownership/assignment before serving private field resources.[^kfm-auth-backend]

---

### ✅ Refresh endpoint flow (high-level)

```ts
import { verifyRefreshToken, issueAccessToken } from './refreshToken';

export async function refresh(req, res) {
  const refreshToken = req.cookies?.refreshToken; // or header/body

  const result = verifyRefreshToken(refreshToken);
  if (!result.ok) return res.status(401).json({ error: 'Invalid refresh token' });

  const accessToken = issueAccessToken({
    sub: result.userId,
    roles: result.roles,
    accessLevels: result.accessLevels,
  });

  return res.status(200).json({ accessToken });
}
```

---

### ✅ Audit event builder

KFM calls out audit logging for security-sensitive actions like login/logout and permission changes.[^kfm-audit]

```ts
import { buildAuditEvent } from './audit';

const evt = buildAuditEvent({
  actorUserId: req.user?.id ?? null,
  action: 'auth.login',
  meta: { ip: req.ip, userAgent: req.headers['user-agent'] },
});
```

---

## 🔒 Security rules (non-negotiable)

- 🚫 **Never log**: passwords, refresh tokens, JWTs, reset tokens, MFA codes  
- 🔐 Use HTTPS/TLS everywhere (UI↔API, API↔services, etc.)[^kfm-security]  
- 🧩 Centralize token verification (middleware/decorator/DI), not ad-hoc per endpoint.[^kfm-auth-backend]  
- ⏱️ Prefer constant-time comparisons for secrets (timing attack resistance)  
- 🕵️ Avoid user enumeration (login/reset should not reveal whether an email exists)  
- 🍪 If using cookies for refresh tokens, evaluate CSRF risk (KFM notes CSRF protection may be needed depending on how cookies are used).[^kfm-security]

---

## 🧪 Testing checklist

✅ Unit tests you should have for every util module:
- Token sign ↔ verify round-trip (good token)  
- Expired token rejection  
- Bad signature rejection  
- Password hash/verify true + false  
- RBAC guard truth table (role × action)  
- MFA verify good/bad codes (if implemented)  
- Audit event shape includes userId + timestamp + action details (and never includes secrets)[^kfm-audit]

---

## 📚 References (project-grounded)

[^kfm-auth-backend]: KFM: token-based auth (JWT), per-request verification, role checks, operational access levels, and service-to-service tokens.:contentReference[oaicite:0]{index=0}
[^kfm-user-auth]: KFM: JWT session tokens, ~1 hour expiry example, refresh tokens, bcrypt/Argon2 hashing, password reset one-time token, lockouts, and MFA options.:contentReference[oaicite:1]{index=1}
[^kfm-security]: KFM: roles/permissions mapping, operational access levels, audit logging, and encryption in transit/at rest considerations.:contentReference[oaicite:2]{index=2}
[^kfm-audit]: KFM: audit logging of security-sensitive actions (login, logout, data modification, permission changes).:contentReference[oaicite:3]{index=3}
[^kfm-arch-utils]: KFM: layered code structure and use of a `utils/` directory for helper functions; keep dependency direction clean (upper layers can import lower layers).:contentReference[oaicite:4]{index=4}
[^kfm-arch]: KFM: architecture principle—inner layers stay decoupled; talk inwards with simple data, talk outwards through interfaces.:contentReference[oaicite:5]{index=5}

