# 🚫 Invalid Serialized Token Fixtures

![fixtures](https://img.shields.io/badge/fixtures-invalid%20tokens-blue)
![format](https://img.shields.io/badge/format-serialized%20%28compact%29-informational)
![security](https://img.shields.io/badge/safety-test--only-red)
![auth](https://img.shields.io/badge/domain-auth%20%26%20security-purple)

> ⚠️ **Test-only fixtures.** Every token in this folder is **intentionally invalid** and must **never** be used in production environments.  
> 🔐 Purpose: prove our auth middleware rejects bad tokens reliably (and *humanely*—clear errors without leaking sensitive details).

---

## 📍 Where you are

```text
📦 api/
└─ 📂 src/
   └─ 📂 auth/
      └─ 📂 tests/
         └─ 📂 fixtures/
            └─ 📂 tokens/
               └─ 📂 serialized/
                  ├─ ✅ valid/
                  └─ 🚫 invalid/   👈 you are here
                     └─ 📄 README.md
```

---

## 🧭 What this folder is for

KFM uses **token-based authentication** (JWT-style session tokens) where clients send a token in requests (commonly via `Authorization: Bearer <token>`). The backend validates the token (signature + expiry + key selection + claim rules) before allowing access. 🛡️

This folder contains **negative test fixtures**: serialized (compact) token strings that should be rejected **every time**, deterministically.

✅ Good uses:
- Validate **parsing** behavior (malformed tokens, invalid base64, invalid JSON).
- Validate **verification** behavior (bad signatures, unknown `kid`, wrong algorithm).
- Validate **claim enforcement** (expired `exp`, future `nbf`, wrong `aud`/`iss`).
- Validate **safe failure** behavior (401 vs 403, stable error codes, no info leaks).

🚫 Not a good place for:
- Real tokens captured from environments
- Any secrets (private keys, production `kid`s, user PII)
- Generated-on-the-fly fixtures with non-deterministic timestamps

---

## 🧩 How tests typically use these fixtures

Most tests will load one of these files as a plain string and inject it into the same surface area the real app uses:

- HTTP header: `Authorization: Bearer <fixture>`
- Cookie-based auth (if applicable)
- WS handshake auth (if applicable)

Example (pseudocode):

```ts
// 1) load fixture from: tokens/serialized/invalid/expired.jwt
// 2) call an endpoint that requires auth
// 3) assert 401 + correct error classification

const token = loadFixture("tokens/serialized/invalid/expired.jwt");

const res = await api.get("/api/protected", {
  headers: { Authorization: `Bearer ${token}` },
});

expect(res.status).toBe(401);
// Prefer stable error codes over brittle message text:
expect(res.body.error.code).toBe("AUTH_TOKEN_EXPIRED");
```

> 💡 Tip: Invalid-token fixtures should usually assert **401 Unauthorized**.  
> Save **403 Forbidden** for *valid token* + *insufficient privileges/roles* scenarios.

---

## 📄 Fixture file contract (keep it boring ✅)

To keep tests stable and portable, fixtures in this directory should follow a simple contract:

- **Encoding:** UTF-8 text
- **Content:** the raw serialized token only
- **Shape:** usually `header.payload.signature` (JWT compact serialization), unless the test is about “not-a-JWT”
- **No wrapping quotes**, no JSON wrapper
- **Single line preferred** (trailing newline is fine)
- **No environment-specific values** (hostnames, prod issuer URLs, real emails, etc.)
- **Deterministic timestamps** (see cookbook below)

> 🧼 If you ever need metadata (why it’s invalid, expected error code), put it here in the README table (or add a small adjacent `*.meta.json` only if the test harness supports it).

---

## 🧪 Recommended invalid cases matrix

Keep this list as your “coverage map” for token rejection. You don’t need every case on day one—add as auth rules evolve. 🧱

| 🧩 Case | 🧨 What’s invalid | ✅ What we’re proving | 🎯 Expected outcome |
|---|---|---|---|
| `malformed__one_segment` | Not 3 segments | Parser rejects non-JWT shape | 401 + `AUTH_TOKEN_MALFORMED` |
| `malformed__too_many_segments` | >3 segments | Parser rejects ambiguous token | 401 + `AUTH_TOKEN_MALFORMED` |
| `base64__invalid_header` | Header not base64url | Decoder hard-fails safely | 401 + `AUTH_TOKEN_DECODE_FAILED` |
| `json__invalid_header` | Header decodes but is not JSON | JSON parsing failure path works | 401 + `AUTH_TOKEN_DECODE_FAILED` |
| `alg__none` | `{"alg":"none"}` | “none” alg is refused | 401 + `AUTH_TOKEN_UNSUPPORTED_ALG` |
| `kid__missing` | No `kid` but we require it | Key selection rules enforced | 401 + `AUTH_TOKEN_KEY_NOT_FOUND` |
| `kid__unknown` | `kid` not in JWKS/test keys | Unknown keys rejected | 401 + `AUTH_TOKEN_KEY_NOT_FOUND` |
| `sig__tampered_payload` | Payload altered after signing | Signature verification works | 401 + `AUTH_TOKEN_BAD_SIGNATURE` |
| `claims__expired` | `exp` in the past | Expiry is enforced | 401 + `AUTH_TOKEN_EXPIRED` |
| `claims__nbf_in_future` | `nbf` in the future | Not-before is enforced | 401 + `AUTH_TOKEN_NOT_YET_VALID` |
| `claims__aud_mismatch` | Wrong/missing `aud` | Audience enforcement works | 401 + `AUTH_TOKEN_INVALID_CLAIMS` |
| `claims__iss_mismatch` | Wrong `iss` | Issuer enforcement works | 401 + `AUTH_TOKEN_INVALID_CLAIMS` |
| `claims__roles_wrong_type` | roles claim is malformed | Claim typing rules enforced | 401 + `AUTH_TOKEN_INVALID_CLAIMS` |
| `token_type__refresh_used_as_access` | Refresh token in access context | Token “purpose” enforcement | 401 + `AUTH_TOKEN_WRONG_TYPE` |

> ✅ When you add a new fixture file, add a row here so future maintainers can see coverage at a glance.

---

## ➕ Adding a new invalid fixture (recipe)

1) **Pick a single failure mode** 🎯  
   Don’t mix issues (e.g., “expired *and* bad signature”) unless the test is explicitly about precedence.

2) **Start from a known-good reference** ✅  
   If `../valid/` exists, copy the closest valid token and mutate it.

3) **Name it like a test case** 🏷️  
   Suggested naming:  
   - `category__specific_reason.jwt`  
   - Keep lowercase, use `__` to separate category/reason.

4) **Add/extend a test** 🧪  
   Assert:
   - rejection outcome (usually 401)
   - stable error code/classification
   - no sensitive info in response body

5) **Document it** 📘  
   Add a row to the matrix above.

---

## 🧰 Token mutation cookbook (quick + deterministic)

<details>
<summary>🧪 Click to expand cookbook</summary>

### 1) Make a bad signature (tamper payload)

- Take a valid token: `header.payload.signature`
- Change **one character** in the payload segment (base64url-safe)
- Keep header and signature as-is

```text
✅ valid:   eyJhbGciOi... . eyJzdWIiOiIxMjMifQ . AbCdEf...
🚫 tamper: eyJhbGciOi... . eyJzdWIiOiIxMjMifR . AbCdEf...
                         ^ flip one char
```

### 2) Make it “not-a-JWT” (shape tests)

```text
🚫 one segment:    just-a-string
🚫 two segments:   header.payload
🚫 four segments:  h.p.s.extra
```

### 3) Expired / not-before tests (avoid clock flake)

For time-based fixtures, tests should freeze time (or use a predictable “now”).
- If your test suite uses time-freezing (e.g., `freezegun`, `jest.useFakeTimers`, etc.), generate tokens relative to that frozen time.
- Otherwise, bake in fixed epoch timestamps and make tests compare against a fixed “now”.

**Rule:** If a test ever fails only on certain days/times, the fixture is not deterministic.

</details>

---

## 🔒 Security & hygiene rules (non-negotiable)

- 🧯 **No production keys**, no real `kid` values that map to real infra
- 🧑‍🌾 **No PII** (emails, real names, phone numbers, real account IDs)
- 🧊 Keep time deterministic (freeze time in tests if needed)
- 🧷 Prefer asserting stable error codes, not string messages
- 🕵️ Don’t leak validation details in responses (e.g., “unknown kid X”)

---

## ✅ Maintenance checklist

- [ ] Each fixture maps to **one** clear failure mode  
- [ ] Each fixture has **at least one** test asserting rejection  
- [ ] Tests assert **status + stable error code**, not brittle message text  
- [ ] Time-based fixtures are **not flaky** (time frozen or fixed epoch)  
- [ ] This README matrix stays in sync with the folder contents  

---

## 🔗 Related folders

- ✅ `../valid/` — known-good serialized tokens (for positive-path tests)
- 🧩 `../../` — token fixture root (other formats, keys, decoded payloads, etc.)

> 🧭 If you add a new fixture “format family” (e.g., decoded payload JSON), put it in a sibling folder and add a README there too—consistent docs make the test suite scale nicely. 🧱✨
