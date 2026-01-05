---
title: "Auth Token Fixtures — Serialized Tokens"
path: "api/src/auth/tests/fixtures/tokens/serialized/README.md"
version: "v0.1.0"
last_updated: "2026-01-04"
status: "active"
doc_kind: "Test Fixture README"
license: "CC-BY-4.0"

# Profile / protocol versions
markdown_protocol_version: "1.0"
pipeline_contract_version: "v13"

# Governance hooks (keep even if repo paths differ; use 'n/a' rather than deleting)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
fair_category: "FAIR+CARE"
care_label: "Public"
sensitivity: "public"
classification: "open"
jurisdiction: "US"

doc_uuid: "urn:kfm:doc:api:auth:tests:fixtures:tokens-serialized:v0.1.0"
commit_sha: "TBD"
doc_integrity_checksum: "sha256:TBD"
---

# 🧾 Auth Token Fixtures — Serialized (Snapshot) Tokens

![scope](https://img.shields.io/badge/scope-tests-blue)
![component](https://img.shields.io/badge/component-auth-purple)
![fixtures](https://img.shields.io/badge/fixtures-serialized%20tokens-orange)

This folder contains **serialized token fixtures** (e.g., compact JWT strings) used by the auth test suite to validate:

- ✅ token verification (signature + algorithm)
- ✅ claim parsing / mapping
- ✅ expiration + refresh behaviors
- ✅ failure modes (bad signature, malformed token, invalid claims, etc.)

> [!IMPORTANT]
> These are **synthetic test artifacts**.  
> Do **not** commit real user tokens, production signing keys, or any secret material into fixtures.

---

## 📘 Overview

### Purpose 🎯

KFM uses JWT tokens for session management (with access token expiry and refresh-token based renewal).  
These fixtures provide **deterministic, file-based examples** so tests can assert behavior without relying on live logins or runtime-generated randomness.

### Scope 🔍

| In Scope ✅ | Out of Scope 🚫 |
|---|---|
| Checked-in token strings used in unit/contract tests | End-to-end login flows (UI ↔ API) |
| “Known-good” tokens for regression coverage | Production key management / real secrets |
| “Known-bad” tokens for error-path coverage | Any PII (emails, names, real IDs, addresses) |
| Companion metadata that makes fixtures reviewable | Load/perf testing |

### Audience 👥

- **Primary:** API/auth developers writing or maintaining tests
- **Secondary:** reviewers validating security posture & CI scans

### Definitions 📚

- **JWT:** JSON Web Token (typically a signed, compact string).
- **Access token:** short-lived token used for API authorization.
- **Refresh token:** longer-lived token used to mint a new access token.
- **Serialized token fixture:** a token stored “as a string” on disk so tests can load it exactly.
- **Fixture:** static test data checked into the repo.

---

## 🗂️ Directory Layout

Path:

```
api/src/auth/tests/fixtures/tokens/serialized/
```

Recommended (CI-friendly) layout:

```
serialized/
├── README.md
├── 📁 valid/
│   ├── access__happy_path__HS256.jwt
│   └── refresh__happy_path__HS256.jwt
├── 📁 invalid/
│   ├── access__expired__HS256.jwt
│   ├── access__bad_signature__HS256.jwt
│   └── access__malformed__jwt.txt
└── 📁 decoded/              # optional (helps code review)
    ├── access__happy_path__HS256.header.json
    ├── access__happy_path__HS256.claims.json
    └── access__happy_path__HS256.notes.md
```

**File format expectations:**

- `*.jwt` / `*.txt` files should contain **exactly one token** on a single line (no wrapping).
- Prefer UTF-8 and avoid extra whitespace; tests should `.trim()` defensively.

> [!TIP]
> If you add a new “weird” fixture (edge-case headers, unusual claim shapes), include a small `*.notes.md`
> explaining **why** it exists and what behavior it is meant to lock in.

---

## 🧪 Fixture Contract

To keep fixtures stable and reviewable:

1. **Deterministic content**  
   - If a claim like `jti` exists, it must be **fixed**, not random.
2. **Pinned time semantics**  
   - `iat`, `exp`, and `nbf` should be pinned to known values; tests should freeze/mock time accordingly.
3. **Safe synthetic identities**  
   - Use obviously fake IDs (e.g., `user_test_001`) and non-real issuers (e.g., `https://example.invalid`).
4. **Test-only signing keys**  
   - Tokens must be signed with test keys that are *not* shared with production.
5. **Naming convention**  
   - Use: `<kind>__<case>__<alg>.<ext>`  
     Example: `access__missing_sub__HS256.jwt`

---

## 🧩 Common Fixture Cases (Cookbook)

| Fixture case | Why we keep it |
|---|---|
| `access__happy_path__*` | baseline “valid token” behavior |
| `refresh__happy_path__*` | validates refresh workflow inputs |
| `access__expired__*` | ensures `exp` is enforced |
| `access__nbf_in_future__*` | ensures `nbf` is enforced (if used) |
| `access__wrong_aud__*` | ensures audience checks work (if configured) |
| `access__wrong_iss__*` | ensures issuer checks work (if configured) |
| `access__missing_sub__*` | ensures required-claim validation |
| `access__bad_signature__*` | ensures signature verification fails correctly |
| `access__malformed__*` | ensures parser errors are handled safely |

> [!NOTE]
> Keep the set lean: add a fixture only when it locks in an important behavior or regression.

---

## 🧪 Using Fixtures in Tests

Typical pattern (illustrative):

```ts
import { readFileSync } from "node:fs";
import path from "node:path";

export function loadSerializedToken(relativeFixturePath: string) {
  return readFileSync(path.join(__dirname, relativeFixturePath), "utf8").trim();
}

// Example
const token = loadSerializedToken("./valid/access__happy_path__HS256.jwt");
```

---

## 🔁 Updating / Regenerating Fixtures

When do you need to update fixtures?

- You changed **claim schema** (new/renamed required claims).
- You changed **signature algorithm** (e.g., HS256 → RS256) or verification rules.
- You changed **expiration / refresh logic**.
- You added new error cases that must remain stable.

Recommended workflow:

1. **Prefer generation over hand-editing**  
   Create/update a small generator script (in the test suite) that produces fixtures from:
   - fixed claim payloads
   - fixed timestamps
   - test-only signing keys
2. **Write both the token and the decoded views** (optional but helpful)
3. **Run auth tests** and ensure failures are meaningful (not just due to clock drift)
4. **Review fixture diffs** like code: token changes should be explainable

Example signing pseudocode (illustrative):

```ts
// Example only — use the signing helper used by this repo.
const accessClaims = {
  sub: "user_test_001",
  roles: ["admin"],
  iss: "https://example.invalid",
  aud: "kfm-api",
  iat: 1700000000,
  exp: 1700003600,
};

const token = signJwt(accessClaims, TEST_ONLY_SIGNING_KEY, { alg: "HS256" });
```

---

## 🔒 Security & CI Notes

Our CI includes automated **secret scanning** and **PII/sensitive data scans**.  
Fixtures are still “real strings”, so treat them as potentially sensitive from a tooling perspective.

**Rules of thumb:**

- ✅ Use **test keys** and synthetic claims only
- ✅ Keep token subjects/IDs non-identifying
- ✅ Avoid embedding URLs/domains that look production-like
- ✅ If a scan flags a fixture, consider:
  - simplifying claims,
  - switching to a clearly fake issuer/audience,
  - or storing decoded JSON + generating the token at test runtime (if deterministic)

> [!CAUTION]
> If you ever see a fixture token that successfully authenticates against a non-test environment,
> treat that as an incident and rotate keys immediately.

---

## ✅ Definition of Done

- [x] YAML front-matter present & populated (use `TBD` / `n/a`, don’t delete fields)
- [x] Required doc sections included (Overview, Layout, etc.)
- [ ] Fixtures contain **no real secrets** (passes secret scanning)
- [ ] Fixtures contain **no PII** (passes sensitive data scanning)
- [ ] Tokens are deterministic (no random IDs/timestamps)
- [ ] Tokens are stored as **single-line** serialized strings (`*.jwt`)
- [ ] Tests passing locally and in CI
- [ ] New edge-cases documented with `*.notes.md` when needed

---

## 📎 References

- JWT + refresh-token based session handling (project security/auth overview).:contentReference[oaicite:0]{index=0}
- CI gates include Markdown protocol/front-matter checks.:contentReference[oaicite:1]{index=1}
- CI security scans include secret scanning + PII/sensitive content scans.:contentReference[oaicite:2]{index=2}
- Front-matter fields + “don’t remove fields” guidance (KFM-inspired template).:contentReference[oaicite:3]{index=3}
