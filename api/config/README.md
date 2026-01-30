# 🔧 `api/config/` — Backend Configuration Hub (KFM)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![PostGIS](https://img.shields.io/badge/PostGIS-336791?logo=postgresql&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?logo=neo4j&logoColor=white)
![OPA](https://img.shields.io/badge/OPA-7D4CDB?logo=openpolicyagent&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?logo=ollama&logoColor=white)

> [!IMPORTANT]
> **This folder is the “single place to look” for how the API gets configured.**  
> KFM is designed so the **UI (and AI) never bypass the API** — configuration must *preserve* that “truth path” and the governance layer. ✅

---

## 📚 Contents

- [🎯 Purpose](#-purpose)
- [🧱 What belongs in `api/config/`](#-what-belongs-in-apiconfig)
- [🧬 Configuration sources & precedence](#-configuration-sources--precedence)
- [🚀 Local dev quickstart](#-local-dev-quickstart)
- [🧪 Environment variables](#-environment-variables)
- [🧠 Focus Mode (AI) configuration](#-focus-mode-ai-configuration)
- [🛡️ Policy & governance config (OPA)](#️-policy--governance-config-opa)
- [🪵 Logging & observability](#-logging--observability)
- [🧯 Troubleshooting](#-troubleshooting)
- [🧩 Adding a new config key](#-adding-a-new-config-key)
- [🔒 Secrets & security rules](#-secrets--security-rules)
- [🔗 Related docs](#-related-docs)

---

## 🎯 Purpose

`api/config/` centralizes **how the FastAPI backend is configured** across:

- 🧑‍💻 **Local dev** (Docker Compose + `.env`)
- 🧪 **CI** (non-interactive environment variables)
- 🚢 **Prod** (secret manager + immutable deployment)

The goal is to keep configuration:

- **Explicit** (no “magic globals” hidden in random modules)
- **Safe-by-default** (fail closed for governance-sensitive concerns)
- **Reproducible** (a configuration change is traceable and reviewable)

---

## 🧱 What belongs in `api/config/`

Think of this directory as the API’s **configuration contract**.

✅ Good candidates:

- Settings loader (env + defaults + validation)
- Structured logging config
- CORS configuration
- DB connection configuration helpers
- Policy engine (OPA) client configuration
- AI routing configuration (Ollama vs OpenAI vs “disabled”)
- Feature flags / environment mode toggles

❌ Not a good fit:

- Business logic (routes/services)
- Secrets (real values)
- Dataset metadata or provenance (that belongs under `data/`)

---

## 🧬 Configuration sources & precedence

**Recommended precedence** (highest wins):

1. **Runtime environment variables** (CI/prod)
2. **`.env` file** (local dev convenience)
3. **Checked-in defaults** (safe, minimal)

> [!TIP]
> Make configuration **visible** by exposing a “read-only config snapshot” endpoint in dev only  
> (e.g., `/debug/config`, with secrets redacted). This saves hours.

---

## 🚀 Local dev quickstart

```bash
# from repository root (recommended workflow)
cp .env.example .env

# bring up the whole stack
docker-compose up --build
```

### Handy URLs (typical)
- ✅ API docs (Swagger): `http://localhost:8000/docs`
- 🧠 GraphQL (if enabled): `http://localhost:8000/graphql`
- 🕸️ Neo4j browser: `http://localhost:7474`
- 🌐 Web dev server (if present): `http://localhost:3000`

> [!NOTE]
> If you change environment variables, you’ll usually need to restart containers:
>
> ```bash
> docker-compose down
> docker-compose up
> ```

---

## 🧪 Environment variables

> [!IMPORTANT]
> **Never commit real secrets**. Use `.env.example` for *templates only*.

### Minimum expected (dev stack)

These are the core “stack wiring” variables you’ll almost always need:

- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `NEO4J_AUTH`

<details>
<summary><strong>📄 Example <code>.env</code> template</strong> (copy/paste)</summary>

```dotenv
# =========================
# 🌱 Environment / Mode
# =========================
APP_ENV=dev
LOG_LEVEL=INFO

# =========================
# 🗺️ Databases
# =========================
POSTGRES_USER=kfm
POSTGRES_PASSWORD=change-me
POSTGRES_DB=kfm

# if your code uses explicit host/port, set them too
POSTGRES_HOST=postgis
POSTGRES_PORT=5432

NEO4J_AUTH=neo4j/test
NEO4J_URI=bolt://neo4j:7687

# =========================
# 🛡️ Policy Engine (OPA)
# =========================
OPA_ENABLED=true
OPA_URL=http://opa:8181
OPA_FAIL_CLOSED=true

# =========================
# 🧠 Focus Mode (AI)
# =========================
AI_ENABLED=false

# Option A: Local Ollama
AI_BACKEND=ollama
AI_BACKEND_URL=http://host.docker.internal:11434
OLLAMA_MODEL=llama2:7b

# Option B: OpenAI (only if permitted)
# AI_BACKEND=openai
# OPENAI_API_KEY=sk-REDACTED
# OPENAI_MODEL=gpt-4o-mini

# =========================
# 🌍 CORS
# =========================
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

</details>

---

## 🧠 Focus Mode (AI) configuration

KFM’s “Focus Mode” should be **governance-aware**: the AI must use approved tools/APIs and return evidence-backed outputs.

### Option A — Local Ollama (recommended for privacy/offline)

1. Install and run Ollama locally:
   ```bash
   ollama serve
   ```

2. Verify the local API is reachable (default is usually port `11434`):
   ```bash
   curl http://localhost:11434
   ```

3. In `.env`, point the API to Ollama:
   ```dotenv
   AI_BACKEND=ollama
   AI_BACKEND_URL=http://host.docker.internal:11434
   OLLAMA_MODEL=llama2:7b
   ```

> [!TIP]
> If the API runs inside Docker, `host.docker.internal` is the typical bridge back to your host machine.
> If your OS doesn’t support it, run Ollama in a container (or add a host mapping).

### Option B — OpenAI (only if allowed)

```dotenv
AI_BACKEND=openai
OPENAI_API_KEY=sk-REDACTED
```

> [!CAUTION]
> Be mindful of cost + data governance when using external AI services.

---

## 🛡️ Policy & governance config (OPA)

A core KFM stance: **the backend consults policy before returning sensitive results** (datasets, AI answers, etc.).

### Recommended policy behaviors

- ✅ **Fail closed**: if OPA is unreachable, deny sensitive actions.
- ✅ **Versioned policy decisions**: log which policy bundle/commit governed a decision.
- ✅ **Sanitization support**: some denials may be partial (mask/round/remove restricted fields).

### Integration patterns

- **Sidecar OPA container** (API calls OPA via HTTP)
- **Embedded OPA evaluation** (WASM or library)

> [!NOTE]
> Policies are the source of truth — configuration should only point the API at the correct policy runtime,
> and define safe defaults for “deny / redact / refuse”.

---

## 🪵 Logging & observability

### Goals
- Trace requests across the stack (API ↔ DB ↔ AI ↔ policy)
- Avoid logging secrets or sensitive payloads
- Make debugging “why was this denied?” easy

### Recommendations
- Use **structured logs** (JSON) in container environments
- Redact:
  - tokens / keys
  - full prompts (unless explicitly dev-only + scrubbed)
  - restricted dataset fields

---

## 🧯 Troubleshooting

### 🔌 Port conflicts
If you already have services on common ports, you may need to adjust Docker mappings:

- Postgres/PostGIS: `5432`
- Neo4j browser: `7474`
- API: `8000`
- Web: `3000`

### ♻️ “I changed `.env` but nothing happened”
Restart containers:

```bash
docker-compose down
docker-compose up
```

### 🧠 “AI backend not reachable from Docker”
- Confirm `ollama serve` is running
- Try using `host.docker.internal`
- Or run Ollama in Compose as a service and set `AI_BACKEND_URL=http://ollama:11434`

---

## 🧩 Adding a new config key

When you add a new configuration value:

1. ✅ Add it to the settings loader (with validation + defaults)
2. ✅ Add it to `.env.example` (template only)
3. ✅ Document it in this README (short + practical)
4. ✅ If security-related, default it to *safe behavior*
5. ✅ Add a test that confirms:
   - it loads from env
   - invalid values fail fast with a clear message

> [!TIP]
> A tiny “config schema test” saves future you from silent misconfigurations.

---

## 🔒 Secrets & security rules

**Rules of the road:**

- ✅ `.env` must be gitignored
- ✅ Never log `OPENAI_API_KEY`, DB passwords, JWT secrets, etc.
- ✅ Prefer secret managers in production (not `.env`)
- ✅ Don’t “helpfully” dump `os.environ` in logs
- ✅ Treat AI prompts/responses as potentially sensitive (they may contain restricted snippets)

---

## 🔗 Related docs

- `docs/architecture/` — system overview & “truth path” design
- `policy/` — Rego policies and governance rules
- `api/` — FastAPI application code (routers/services)
- `pipelines/` + `data/` — ingestion, catalog, provenance, and storage workflows

---

### ✅ Checklist (quick sanity)

- [ ] `.env` exists (local dev) and secrets aren’t committed
- [ ] API starts cleanly with Compose
- [ ] Swagger UI loads at `http://localhost:8000/docs`
- [ ] OPA reachable (or safely fails closed)
- [ ] AI disabled by default unless configured