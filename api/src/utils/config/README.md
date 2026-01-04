# ⚙️ Config Utilities (`api/src/utils/config`)

![module](https://img.shields.io/badge/module-config-6f42c1?style=flat-square) ![scope](https://img.shields.io/badge/scope-api-1f6feb?style=flat-square) ![layer](https://img.shields.io/badge/layer-utils-22c55e?style=flat-square)

Centralized, **typed**, and **validated** runtime configuration for the API — with a security-first posture 🔐 and clean-architecture-friendly boundaries 🧱.

> [!IMPORTANT]
> **Do not** read `process.env` directly outside this folder.  
> Import configuration from this module so the API stays **deterministic**, **testable**, and **safe-by-default**.

---

## 🧭 What this folder is responsible for

✅ **Single source of truth** for configuration values  
✅ **Type coercion** (string → number/boolean/list/URL)  
✅ **Validation** (fail-fast on invalid/missing required config)  
✅ **Safe access patterns** (no secrets in logs, no accidental client exposure)  
✅ **Environment segmentation** (dev / test / prod)  

🚫 Not responsible for business logic, feature implementation, DB queries, etc.

---

## 🧠 Design rules (KFM-aligned)

### 1) Keep secrets server-side 🔐
- API keys, credentials, tokens, and service accounts must remain in backend configuration only.
- Never embed secrets in code or version control.
- Prefer environment variables or a secrets manager (vault/service) at runtime.

> [!NOTE]
> If the frontend needs any config-like value, it must be **explicitly whitelisted** and transported through a controlled endpoint — never “dump config”.

### 2) Fail fast at startup 🧨
If config is missing or malformed, the API should exit on boot with a clear error message.

### 3) Keep layers clean 🧱
- `config` is a **utility**: higher layers depend on it, but it should not import from business/domain layers.
- Prefer passing config into service constructors/functions (Dependency Inversion) rather than importing everywhere.

---

## 📁 Suggested layout

> Your exact file names may differ — keep the responsibilities consistent ✅

```text
📁 api/
  📁 src/
    📁 utils/
      📁 config/
        ├─ 📄 README.md              # you are here 🙂
        ├─ 📄 index.ts               # public exports
        ├─ 📄 load-env.ts            # optional .env loader (dev/test only)
        ├─ 📄 schema.ts              # validation rules (zod/joi/custom)
        ├─ 📄 config.ts              # typed config object
        ├─ 📄 redact.ts              # safe logging helpers (optional)
        └─ 📁 __tests__/             # config tests (optional)
```

---

## 🚀 Quick start

### Import config (✅ preferred)
```ts
import { config } from '@/utils/config';

// Example usage
app.listen(config.http.port, config.http.host);
```

### Don’t do this (🚫 scattered env access)
```ts
// ❌ Avoid reading env in random places
const port = process.env.PORT;
```

---

## 🧪 Validation + typing conventions

### Recommended behavior
- Parse env vars **once** at boot.
- Convert into correct types (numbers, booleans, URLs).
- Return a **frozen** config object to prevent runtime mutation.

### Type parsing patterns (examples)
- `PORT="3000"` → `number`
- `DEBUG="true"` → `boolean`
- `ALLOWED_ORIGINS="https://a.com,https://b.com"` → `string[]`
- `DATABASE_URL="postgres://..."` → validated string/URL

> [!TIP]
> Keep config “shape” stable. Adding new keys is fine; renaming/removing keys should be treated like a breaking change.

---

## 🧾 Environment variables

Because environments evolve, treat this as a **template** (not a hard contract). Add/remove keys as the API’s integrations grow.

<details>
<summary><strong>📄 Example .env template (adjust to your stack)</strong></summary>

```bash
# 🌍 Runtime
NODE_ENV=development
LOG_LEVEL=debug

# 🌐 HTTP
API_HOST=0.0.0.0
API_PORT=3000
API_BASE_URL=http://localhost:3000

# 🗄️ Database
DATABASE_URL=postgres://user:pass@localhost:5432/kfm

# 🔐 Auth / sessions
JWT_SECRET=change-me
SESSION_SECRET=change-me-too

# 🛰️ External services (server-only)
GOOGLE_EARTH_ENGINE_KEY=...
WEATHER_PROVIDER_API_KEY=...
```
</details>

---

## 🔐 Secrets & safe logging

### Rules
- Never print full config to logs.
- If you must log configuration, log **only** non-sensitive fields and **redact** secrets.

✅ Good:
```ts
logger.info('config loaded', { env: config.runtime.env, port: config.http.port });
```

🚫 Bad:
```ts
logger.info({ config }); // ❌ could leak secrets
```

> [!IMPORTANT]
> Treat secrets as **tainted**. The only safe default is “do not log”.

---

## 🧩 Adding a new config value (the safe path)

1) **Define the env var name**
   - Use `UPPER_SNAKE_CASE`
   - Prefer a stable prefix if your repo uses one (ex: `KFM_`, `API_`)

2) **Add to schema/validator**
   - Mark required vs optional
   - Add type conversion and constraints (min/max, URL format, allowed enums)

3) **Expose through typed config**
   - Keep structure organized (e.g., `config.http.*`, `config.db.*`, `config.auth.*`)

4) **Update docs**
   - Add to this README template (or your `.env.example`)

5) **Add/adjust tests**
   - Validate failure modes (missing required vars)
   - Validate parsing (string → number/boolean/list)

✅ Checklist:
- [ ] Schema updated
- [ ] Config object updated
- [ ] `.env.example` updated (if present)
- [ ] Tests updated
- [ ] No secret committed 🚫

---

## 🐳 Docker / Compose notes

When running in containers:
- Prefer injecting env via `docker compose` / CI env settings / secrets manager.
- Validate config at startup exactly the same way as local.

Handy commands:
```bash
# inspect computed compose config
docker-compose config

# view logs
docker-compose logs

# rebuild + recreate containers
docker-compose up -d --build
```

---

## 🩺 Troubleshooting

### “It works locally but fails in CI/Prod”
- Check that required env vars exist in the deployment environment.
- Ensure secrets are injected via your CI/CD or vault mechanism.
- Confirm `.env` loading is only used for local/dev/test (not relied on in prod).

### “Config says PORT is invalid”
- Make sure parsing converts to a number and validates range (1–65535).
- Verify you didn’t include whitespace: `PORT="3000 "`.

### “A secret showed up in logs”
- Add/redesign redaction helpers.
- Audit log calls for accidental `logger.debug({ config })`.

---

## 📚 References (project docs)

- `Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf`
- `Scientific Method _ Research _ Master Coder Protocol Documentation.pdf`
- `Introduction-to-Docker.pdf`

> [!NOTE]
> This module is intentionally small and boring 😄 — boring config is stable config.

