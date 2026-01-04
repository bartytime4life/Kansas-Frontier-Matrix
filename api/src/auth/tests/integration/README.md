<a id="top"></a>

<div align="center">

# 🔐 Auth Integration Tests

<p>
  <img alt="scope" src="https://img.shields.io/badge/scope-auth-purple" />
  <img alt="tests" src="https://img.shields.io/badge/tests-integration-blue" />
  <img alt="security" src="https://img.shields.io/badge/security-JWT%20%2B%20Refresh-orange" />
  <img alt="db" src="https://img.shields.io/badge/db-PostgreSQL-336791" />
  <img alt="dev" src="https://img.shields.io/badge/dev-Docker-2496ED" />
</p>

<p><code>api/src/auth/tests/integration/</code></p>

</div>

> [!NOTE]
> These tests validate the **Auth module as a running system** (HTTP layer ➜ database ➜ token issuance ➜ role checks).  
> If you only need logic validation (no DB / no HTTP), prefer **unit tests** closer to the service layer.

> [!IMPORTANT]
> Integration tests must run against a **dedicated test database**. Never point these tests at dev/stage/prod data.

---

## 🧭 Quick navigation
- [✅ What we cover](#what-we-cover)
- [🔁 How auth works in KFM](#how-auth-works-in-kfm)
- [🚀 Run locally](#run-locally)
- [🐳 Run in Docker (CI-like)](#run-in-docker-ci-like)
- [🔧 Environment variables](#environment-variables)
- [🧪 Test patterns & conventions](#test-patterns--conventions)
- [🐞 Debugging](#debugging)
- [🧯 Troubleshooting](#troubleshooting)
- [🧩 Contribution checklist](#contribution-checklist)

---

<a id="what-we-cover"></a>

## ✅ What we cover

### 🎯 Core scenarios (must-have)
- **Login** returns an *access token* + *refresh token* ✅
- **Refresh** returns a *new access token* ✅
- **Protected endpoints** reject missing/invalid/expired JWT ✅
- **Role-protected endpoints** return **403** when the user lacks permissions ✅

### 🛡️ Security & abuse (highly recommended)
- Invalid credentials return **401** (and never leak which field was wrong)
- Optional: rate limiting / lockout behavior after repeated failed logins
- Refresh token invalidation (logout / rotation), if implemented
- Audit / logging basics (no token leakage in logs)

### 👤 User lifecycle (optional, if implemented)
- Password reset request creates a one-time token and allows password change
- Email verification flow

#### 📌 Suggested test matrix
| Area | Endpoint examples (adjust to actual routes) | Minimum assertions |
|---|---|---|
| Login | `POST /api/auth/login` | `200`, tokens exist, token claims include roles |
| Refresh | `POST /api/auth/refresh` | `200`, new access token differs, old token can expire |
| RBAC | `GET /api/admin/*` | `403` for non-admin, `200` for admin |
| JWT guard | `GET /api/me` | `401` without token, `200` with token |
| Reset | `POST /api/auth/password-reset/*` | token issued, token consumed once |

---

<a id="how-auth-works-in-kfm"></a>

## 🔁 How auth works in KFM

KFM uses a **token-based** auth model:

- Users authenticate via a login endpoint and receive a **signed JWT** that includes user identity + roles.
- JWTs are short-lived and are renewed via a **refresh token** mechanism.
- Passwords are stored as **strong hashes** (bcrypt / Argon2), and user accounts map to roles like *farmer*, *researcher*, *admin*.

### 🧾 Header convention
For protected calls, clients should send the access token in:
- `Authorization: Bearer <accessToken>`

### 🧠 Token flow (mental model)

```mermaid
sequenceDiagram
  autonumber
  participant C as Client (Web / Mobile)
  participant A as Auth API
  participant U as User Store (DB)

  C->>A: POST /auth/login (username + password)
  A->>U: Verify user + password hash
  U-->>A: userId + roles
  A-->>C: accessJWT (exp) + refreshToken

  C->>A: GET /protected (Authorization: Bearer accessJWT)
  A-->>C: 200 OK (if allowed)

  C->>A: POST /auth/refresh (refreshToken)
  A-->>C: new accessJWT
```

> [!TIP]
> For refresh-token tests, it’s common to shorten access-token TTL in test config so you can verify expiry + refresh quickly.

---

<a id="run-locally"></a>

## 🚀 Run locally

### ✅ Prereqs
- Node.js (LTS) + npm
- Docker (recommended for a disposable Postgres)
- A test env file (ex: `.env.test`) or exported env vars

---

### 1) Start the test database (recommended: Docker)

If the repo already ships a compose file for tests, use it.

If you need a quick one, drop a `docker-compose.test.yml` near the API root:

```yaml
version: "3.9"
services:
  test-db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_USER: kfm_test
      POSTGRES_PASSWORD: kfm_test
    ports:
      - "54322:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U kfm_test"]
      interval: 2s
      timeout: 2s
      retries: 15
```

Run it:

```bash
docker compose -f docker-compose.test.yml up -d test-db
```

---

### 2) Run migrations / bootstrap (if applicable)

Depending on our DB layer, you may need one of these (pick what matches our stack):

```bash
# Example patterns — adjust to our repo scripts/tools:
npm run db:migrate:test
npm run db:seed:test
```

---

### 3) Execute only Auth integration tests

Pick the command that matches our test runner:

```bash
# Jest (common)
npx jest src/auth/tests/integration --runInBand

# Or via npm scripts (preferred if configured)
npm run test:integration -- src/auth/tests/integration
```

> [!NOTE]
> `--runInBand` is recommended if parallel workers would collide on the same DB/schema.

---

<a id="run-in-docker-ci-like"></a>

## 🐳 Run in Docker (CI-like)

This is useful when you want your local run to behave like CI.

<details>
<summary><strong>Example docker-compose (app + test-db + test runner)</strong></summary>

```yaml
version: "3.9"
services:
  test-db:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: kfm_test
      POSTGRES_USER: kfm_test
      POSTGRES_PASSWORD: kfm_test

  api:
    build: .
    environment:
      NODE_ENV: test
      DATABASE_URL: postgres://kfm_test:kfm_test@test-db:5432/kfm_test
    depends_on:
      test-db:
        condition: service_started

  test:
    build:
      context: .
      dockerfile: Dockerfile.test
    environment:
      NODE_ENV: test
      DATABASE_URL: postgres://kfm_test:kfm_test@test-db:5432/kfm_test
    depends_on:
      - api
      - test-db
    command: ["npm", "run", "test"]
```

</details>

Run:

```bash
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit
```

---

<a id="environment-variables"></a>

## 🔧 Environment variables

At minimum, integration tests need a DB connection and auth secrets that are **safe for test**.

| Variable | Required | Example | Why it exists |
|---|:---:|---|---|
| `NODE_ENV` | ✅ | `test` | Enables test-only configuration paths |
| `DATABASE_URL` | ✅ | `postgres://user:pass@localhost:54322/kfm_test` | Real DB for integration tests |
| `JWT_SECRET` | ✅ | `test-only-secret` | Signing access JWTs |
| `JWT_EXPIRES_IN` | ⛳ | `1h` | Access token TTL (often shortened in tests) |
| `REFRESH_TOKEN_SECRET` | ✅ | `test-only-refresh-secret` | Signing/encrypting refresh tokens |
| `REFRESH_EXPIRES_IN` | ⛳ | `30d` | Refresh TTL |
| `PASSWORD_HASH_COST` | ⛳ | `4` | Lower cost speeds tests (but keep logic consistent) |

> [!TIP]
> Keep test secrets in `.env.test` and ensure CI injects them securely (never commit real secrets).

---

<a id="test-patterns--conventions"></a>

## 🧪 Test patterns & conventions

### 🗂️ Suggested folder layout (recommended)

```
📦 api/
 └─ 📂 src/
    └─ 📂 auth/
       └─ 📂 tests/
          └─ 📂 integration/
             ├─ 📄 README.md  👈 you are here
             ├─ 🧪 login.int.test.ts
             ├─ 🧪 refresh.int.test.ts
             ├─ 🧪 rbac.int.test.ts
             ├─ 📂 helpers/
             │  ├─ 🧰 createTestApp.ts
             │  ├─ 🧰 db.ts
             │  └─ 🧰 tokens.ts
             └─ 📂 fixtures/
                └─ 👤 users.ts
```

### 🧱 Golden rules
- **Test at the boundary**: treat the API like a client would (HTTP requests + real DB).
- **One assertion target per test**: keep tests small and focused.
- **Reset state**: every test should leave the DB clean.
  - Prefer transactions + rollback, or truncate tables in `afterEach`.
- **Never assume ordering**: integration tests must be order-independent.
- **Avoid token snapshots**: validate claims/structure instead of exact string matches.

### 🧪 Example test skeleton (Jest + Supertest style)

```ts
/**
 * NOTE: This is a template — adjust imports/helpers to match the repo.
 */
import request from "supertest";
import { createTestApp } from "./helpers/createTestApp";
import { seedUser } from "./fixtures/users";

describe("Auth: login", () => {
  it("returns access + refresh tokens for valid credentials", async () => {
    const app = await createTestApp();

    await seedUser({
      email: "farmer@example.com",
      password: "Password123!",
      roles: ["farmer"],
    });

    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "farmer@example.com", password: "Password123!" });

    expect(res.status).toBe(200);
    expect(res.body.accessToken).toBeDefined();
    expect(res.body.refreshToken).toBeDefined();
  });
});
```

---

<a id="debugging"></a>

## 🐞 Debugging

### ▶️ Run a single test file
```bash
npx jest src/auth/tests/integration/login.int.test.ts --runInBand
```

### 🧷 Attach a debugger
```bash
node --inspect-brk ./node_modules/.bin/jest src/auth/tests/integration/login.int.test.ts --runInBand
```

Then open Chrome DevTools for Node and set breakpoints.

> [!TIP]
> If a test is flaky, add temporary logs around **token issuance**, **DB cleanup**, and **clock/time handling**.

---

<a id="troubleshooting"></a>

## 🧯 Troubleshooting

- **DB connection refused**  
  ✅ Confirm Postgres is running and `DATABASE_URL` host/port matches your compose mapping.

- **Tests hang on startup**  
  ✅ The DB may not be “ready” yet. Add a healthcheck (see compose example) or a wait-for script.

- **Parallel tests collide**  
  ✅ Run with `--runInBand` or allocate a unique schema/database per worker.

- **“Works locally, fails in CI”**  
  ✅ Ensure CI spins up the same disposable DB and exports the same env vars used in `.env.test`.

---

<a id="contribution-checklist"></a>

## 🧩 Contribution checklist

- [ ] Added/updated integration tests for new auth behavior
- [ ] Tests pass locally **and** in Docker/CI mode
- [ ] DB state is cleaned up after each test
- [ ] No secrets or tokens committed/logged
- [ ] Updated this README if run instructions changed

---

<p align="right"><a href="#top">⬆️ Back to top</a></p>
