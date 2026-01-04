# 🔑 Auth Test Key Fixtures (`fixtures/keys`)

![Scope](https://img.shields.io/badge/scope-tests-blue)
![Security](https://img.shields.io/badge/security-non--production-orange)
![Auth](https://img.shields.io/badge/auth-JWT-purple)

> ⚠️ **Test-only cryptographic material**  
> Everything in this folder exists **only** to make authentication tests deterministic.  
> **Never** reuse these keys in dev/staging/prod, and **do not** copy them into any runtime secrets store.

---

## 🎯 Purpose

KFM uses **token-based authentication** and (typically) **JWTs** for session management — the server issues a **signed token** containing user identity + roles/claims, and the backend verifies the token’s **signature + expiry** on requests. ✅  
Tests need stable keys so they can reliably:
- sign “known-good” JWTs
- validate signature verification paths
- validate role/claim handling (e.g., `admin`, `researcher`, `user`)
- simulate expiration + refresh behavior without calling external identity providers

---

## 📦 What belongs in this folder

This directory should contain **only** fixtures that are safe to commit and safe to ship with test bundles.

Typical contents (filenames may differ — treat this as the *shape*, not the *truth*):

```text
🧪 api/
└─ 🧩 src/
   └─ 🛡️ auth/
      └─ 🧫 tests/
         └─ 🧰 fixtures/
            └─ 🔑 keys/                              # 👈 test-only signing material (deterministic)
               ├─ 📝 README.md                        # documentation + rules (you are here)
               ├─ 🔐 jwt.test.private.pem             # private signing key (tests only — NEVER prod)
               ├─ 🛂 jwt.test.public.pem              # public verification key (paired with private)
               └─ 🗝️ jwks.test.json                   # optional JWKS fixture ("kid" resolution / JWKS tests)
```

### ✅ Good fixture properties
- **Deterministic**: keys do not change unless we intentionally rotate them for tests
- **Explicitly labeled**: file names and comments scream “TEST”
- **Algorithm-aligned**: matches what the auth module expects (ex: RS256 / ES256 / HS256)
- **Scoped**: used only from `api/src/auth/tests/**` (not production code)

---

## 🧪 How tests should use these keys

### Recommended pattern
- Keep a **single token factory helper** in tests that:
  - loads the fixture key(s)
  - generates JWTs with consistent defaults
  - allows overrides for edge cases (expired token, missing claim, wrong issuer, etc.)
- Keep the application’s runtime configuration (env, secret manager, etc.) **out of tests** unless explicitly testing config behavior.

### Example JWT claim sets (illustrative)
```json
{
  "sub": "user_123",
  "roles": ["researcher"],
  "iat": 1735689600,
  "exp": 1735693200,
  "iss": "kfm-auth",
  "aud": "kfm-api"
}
```

> 💡 Tip: For expiry tests, freeze time (or inject a clock) so you’re not fighting flaky “it expired 1 second earlier” failures.

---

## 🔄 Regenerating keys (only when necessary)

> ✅ Prefer **not** rotating test keys unless an algorithm/format change forces it.  
> Changing keys often breaks snapshots, hard-coded `kid`s, and token fixtures.

<details>
<summary><strong>Option A: RSA (RS256) via OpenSSL</strong> 🔐</summary>

```bash
# 1) Generate a private key (RSA 2048)
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out jwt.test.private.pem

# 2) Extract the public key
openssl pkey -in jwt.test.private.pem -pubout -out jwt.test.public.pem

# 3) (Optional) sanity check
openssl pkey -in jwt.test.private.pem -text -noout
openssl pkey -in jwt.test.public.pem  -pubin -text -noout
```

**After regenerating:**
- update any `kid` references (if you use JWKS)
- update snapshots / golden tokens
- run the full auth test suite

</details>

<details>
<summary><strong>Option B: EC (ES256) via OpenSSL</strong> ⚡</summary>

```bash
# 1) Generate an EC private key (P-256)
openssl ecparam -name prime256v1 -genkey -noout -out jwt.test.private.pem

# 2) Extract the public key
openssl ec -in jwt.test.private.pem -pubout -out jwt.test.public.pem
```

Only use ES256 if the auth implementation is explicitly configured for it.

</details>

---

## 🧩 If you also maintain a JWKS fixture (`jwks.test.json`)

If your auth system supports `kid` + JWKS discovery, keep your JWKS fixture aligned with:
- algorithm (`alg`)
- key type (`kty`)
- curve/modulus fields (`crv`, `x`, `y` for EC; `n`, `e` for RSA)
- `kid` used in token headers during tests

> 🧠 Rule of thumb: **the token header `kid` must resolve to a matching public key in JWKS**.

---

## 🛡️ Security & repo hygiene rules

### ✅ Allowed here
- **Test-only** keys that cannot unlock any real data or service

### ❌ Not allowed here
- production/staging secrets (ever)
- `.env` files containing secrets
- private keys used by deployed services
- tokens copied from real systems

### CI / scanning note
Many repos run secret scanners during CI. If scanners flag this folder:
- prefer configuring an explicit allowlist rule for **this specific path**
- do **not** “fix” the warning by moving these keys into runtime secrets (that defeats the purpose of deterministic tests)

---

## 🔗 Related KFM docs (repo-root links)

- 📘 Pipeline & governance overview: `/docs/MASTER_GUIDE_v13.md`
- 🧭 Markdown conventions: `/docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
- 🔐 Security policy (if present): `/.github/SECURITY.md`
- ⚖️ Governance & ethics (if present): `/docs/governance/`

---

## ✅ Definition of Done (for changes in this folder)

- [ ] Keys are clearly labeled **TEST ONLY**
- [ ] Filenames match what test helpers/config expect
- [ ] Auth tests pass locally + in CI
- [ ] Any JWKS `kid` / headers are updated and consistent
- [ ] No production secrets were introduced
- [ ] This README updated if behavior/format changed

