# 🧾 Contract Test Config (`api/tests/contract/config`)

| ✅ Purpose | 🧩 Scope | 🔒 Secrets | 🧪 CI Gate |
|---|---|---|---|
| Centralize contract-test settings | API contract verification | **Never** commit tokens/keys | Failures should block merges |

This directory is the **single home** for configuration that powers **API contract tests** (a.k.a. “does the API still behave exactly like the contract says?”). In KFM, the philosophy is **contract-first**: schemas/specs are first-class artifacts, and changes to contracts trigger compatibility and versioning checks.  [oai_citation:0‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🎯 Overview

Contract tests exist to protect the **API boundary** by continuously validating that endpoints match the declared **OpenAPI spec** or **GraphQL schema** and remain **backwards-compatible** unless a deliberate version bump is performed.  [oai_citation:1‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

In CI, the contract-test gate is expected to:
- build/deploy the API (test environment or mocked data),  
- run contract tests against known inputs,  
- lint the OpenAPI/GraphQL definitions,  
- and **block merges** when the contract unexpectedly breaks.  [oai_citation:2‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧭 Canonical “Source of Truth” for Contracts

Contract artifacts (OpenAPI YAML / GraphQL SDL) should live in the API layer’s canonical contract home (e.g., `src/server/contracts/` or equivalent). This config folder should **point to those artifacts**, not duplicate them.  [oai_citation:3‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

> 🧠 If you discover contracts stored in multiple places, consolidate: KFM’s rule is **one canonical location per major component**.  [oai_citation:4‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🗂️ Directory Layout

This folder is intentionally small and boring. Typical layout (names may vary by runner, but **keep the intent** the same):

```text
api/
  tests/
    contract/
      config/
        README.md                    👈 you are here
        local.example.json           🧪 local dev config (safe defaults)
        ci.example.json              🤖 CI config (no secrets)
        staging.example.json         🚦 staging config (no secrets)
        .env.example                 🔐 env var names ONLY (no real values)
        schemas/
          contract-test-config.schema.json  📜 optional config validation schema
```

✅ Guiding rule: **profiles are public**, secrets stay in **environment variables**.

---

## ⚙️ What This Config Should Define

Contract tests should be able to run **deterministically** against a known target. At a minimum, config should answer:

### 1) Target API
- `baseUrl` (e.g., `http://localhost:8080`)
- optional `basePath` (if the API is mounted under `/api`)

### 2) Contract Artifact Inputs
- `openapiSpecPath` **or** `graphqlSchemaPath`
- optional: `contractVersion` (helps smoke-check you’re targeting the right major)

📌 KFM framing: OpenAPI/GraphQL **is the contract**, and breaking it should require versioning or explicit updates.  [oai_citation:5‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:6‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### 3) Auth Mode (no secrets in files)
- `auth.mode`: `none | bearer | basic | apiKey | oauth2` (whatever your API supports)
- `auth.*` should reference **env var names**, not literal tokens

### 4) Stability Controls
- timeouts, retries, and a **bounded** rate limit
- deterministic fixtures/seeds (if your contract tests depend on seeded data)

### 5) Reporting
- machine-readable output (JUnit, JSON, etc.) so CI can annotate failures

---

## 🧬 Recommended Config Shape (Example)

> This is an **example schema**, not a hard requirement. Align it to your actual runner.

```json
{
  "profile": "local",
  "target": {
    "baseUrl": "http://localhost:8080",
    "basePath": "/api"
  },
  "contracts": {
    "openapiSpecPath": "src/server/contracts/openapi.yaml"
  },
  "auth": {
    "mode": "bearer",
    "tokenEnv": "KFM_API_TOKEN"
  },
  "timeouts": {
    "requestMs": 10000,
    "suiteMs": 300000
  },
  "retries": {
    "network": 1,
    "idempotentOnly": true
  },
  "fixtures": {
    "seed": "minimal",
    "resetBetweenTests": true
  },
  "reporting": {
    "format": "junit",
    "outputPath": "api/tests/contract/reports/junit.xml"
  }
}
```

---

## 🧩 Config Resolution Order

Keep overrides predictable (especially for CI). Suggested precedence:

1. CLI flags (highest priority)
2. Environment variables
3. Profile config file (e.g., `local.json`)
4. Defaults in the runner (lowest priority)

```mermaid
flowchart TD
  A[Start contract test runner] --> B{Profile selected?}
  B -->|env/flag| C[Load profile config file]
  B -->|no| D[Use default profile]
  C --> E[Apply env var overrides]
  D --> E[Apply env var overrides]
  E --> F[Apply CLI overrides]
  F --> G[Validate config (optional schema)]
  G --> H[Run contract tests]
```

---

## 🌍 Environments & Profiles

KFM practice is to keep environment configuration **separate** (dev/test/prod), commonly via config files and/or environment variables.  [oai_citation:7‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

### Suggested profiles
- `local` 🧑‍💻: points to a local API instance
- `ci` 🤖: points to CI-spun services (or mocked API)
- `staging` 🚦: points to staging deployments (non-prod)
- `prod` 🏛️: **usually read-only checks only** (avoid destructive tests)

> 🧯 Contract tests should never require “real” production secrets in git. If a prod smoke check is needed, it should use narrowly scoped credentials injected by CI.

---

## 🧪 Running Contract Tests

Your repo may implement contract tests in different runners (Node, Python, etc.). The **configuration goal stays the same**: select a profile + target URL + contract artifact and run.

### Common patterns
```bash
# Option A: profile via env var (example)
CONTRACT_TEST_PROFILE=local CONTRACT_TEST_BASE_URL=http://localhost:8080 \
  ./run-contract-tests.sh

# Option B: profile via CLI (example)
./run-contract-tests.sh --profile ci --base-url "$CI_API_URL"
```

If your workflow uses containers, KFM expects Dockerized components and Compose/K8s manifests to support local dev/test stacks.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)

---

## 🔐 Security & “No Secrets” Rule

CI includes automated secret scanning to prevent API keys/passwords/tokens from being committed in code or config. Treat this directory as **public-by-default**.  [oai_citation:9‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

✅ Do:
- commit `*.example.*` files
- reference secrets by **env var name**
- document required env vars in `.env.example`

❌ Don’t:
- commit tokens, passwords, private keys
- embed production URLs that imply privileged access (unless explicitly approved)

---

## 🧱 When You Change an Endpoint

Use this checklist to keep KFM’s “contract-first” pipeline happy:

1. Update the OpenAPI/GraphQL contract artifact
2. Update/extend contract tests + fixtures for the new behavior
3. Confirm backwards compatibility or bump version explicitly
4. Run contract tests locally + in CI

KFM rule: contract changes must be tested against known inputs/outputs to ensure consistency, and breaking changes require explicit versioning strategy.  [oai_citation:10‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:11‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

---

## 🧯 Troubleshooting

### “Spec mismatch” / “schema validation failed”
- You likely updated implementation but not the contract artifact (or vice versa).
- Confirm your config points at the correct canonical contract path (`src/server/contracts/...`).  [oai_citation:12‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### “401/403 Unauthorized”
- Confirm `auth.mode` is correct
- Confirm CI injected the expected env var(s)
- Verify you didn’t commit secrets (CI may block you even if tests pass).  [oai_citation:13‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)

### “Flaky tests in CI”
- Prefer mocked/test data targets (CI can run contract tests against a test environment or mocked data).  [oai_citation:14‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)
- Reduce dependence on clock time, ordering, and random IDs.

---

## 📚 References (Project Files)

- 📘 Kansas Frontier Matrix — Technical Documentation  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)  [oai_citation:16‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-Bro83fTiCi9UUVVno1fL6L)
- 🧭 KFM Master Guide v13 (Markdown Guide extract)  [oai_citation:17‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)  [oai_citation:18‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:19‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU) [oai_citation:20‡MARKDOWN_GUIDE_v13.md.gdoc](file-service://file-UYVruFXfueR8veHMUKeugU)