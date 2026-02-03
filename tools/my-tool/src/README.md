# 🧰 my-tool · `src/`

> Internal source package for **my-tool** — a developer utility that helps you interact with the **Kansas Frontier Matrix (KFM)** stack in a **contract-first** + **evidence-first** way. 🧭📌

---

## 🎯 What this folder is for

This `src/` directory is the **implementation layer** for the tool:

- 🧩 CLI command implementations (routing, args, help text)
- 🔌 API client wrappers (REST + GraphQL)
- 🧾 “Evidence-first” helpers (attach provenance pointers to output)
- 🧰 Utilities (logging, config, formatting, error handling)

> 💡 If you’re looking for user-facing install/usage docs, check for a higher-level README at `tools/my-tool/README.md` (if present). This file is intentionally **developer-oriented**.

---

## 🧠 Principles (non‑negotiable)

KFM’s philosophy is **traceable output** and **repeatable workflows** — this tool should mirror that.

1. **Evidence-first output 🧾**
   - Every emitted artifact (JSON, markdown, reports) should be traceable to **dataset IDs**, **STAC items/assets**, **DCAT metadata**, and/or **PROV lineage**.
2. **No pipeline leapfrogging 🚦**
   - Canonical ordering (don’t bypass stages):  
     `ETL → STAC/DCAT/PROV → Neo4j Graph → APIs → UI → Story Nodes → Focus Mode`
3. **Safe-by-default 🔒**
   - Validate inputs, use allow-lists, avoid dangerous shell execution patterns, and prefer parameterized queries.
4. **Automation-ready 🤖**
   - Must run cleanly in **local dev** and **CI** with deterministic outputs.

---

## 🧭 Architecture at a glance

```mermaid
flowchart LR
  A[🧰 my-tool CLI / lib] --> B[🌐 KFM REST API]
  A --> C[🧠 KFM GraphQL API]
  B --> D[(🗺️ PostGIS)]
  B --> E[(🧬 Neo4j)]
  B --> F[✨ Focus Mode AI (RAG)]
  F --> G[🦙 Ollama (local LLM) / external provider]
```

---

## 🔌 KFM surfaces you’ll likely touch

Below are **common** API surfaces you’ll see referenced across commands and clients:

### 🗃️ Catalog & datasets
- `GET /api/v1/datasets/{id}`
- `GET /api/v1/catalog/search`
- `GET /api/v1/datasets/{id}/data?format=geojson&bbox=...`

### 🧪 Safe ad‑hoc querying
- `GET /api/v1/query?table=...&select=...&where=...&bbox=...`

### 🧱 Map tiles
- `GET /tiles/{layer}/{z}/{x}/{y}.pbf` (vector tiles)
- `GET /tiles/{layer}/{z}/{x}/{y}.png` (raster tiles)

### 🧠 Focus Mode AI
- `POST /api/v1/ai/query` (answer + citations)
- `/api/v1/ai/stream` (streaming; experimental)
- `GET /api/v1/ai/suggestions`

### 🏗️ Ingestion / pipeline control (restricted)
- `POST /api/v1/ingest/runPipeline`

> ⚠️ Some endpoints are role-gated. Keep tokens out of logs and never print secrets.

---

## 🏃 Local dev quickstart

### 1) Run the KFM stack 🐳
From the repo root (or wherever your `docker-compose.yml` lives):

```bash
docker-compose up
```

Verify:
- ✅ Swagger UI: `http://localhost:8000/docs`
- ✅ GraphQL (if enabled): `http://localhost:8000/graphql`

### 2) Install my-tool deps 📦
From `tools/my-tool/`:

```bash
npm install
```

### 3) Run dev mode ⚡
Choose the command that matches your implementation:

```bash
# Common (TypeScript / watcher)
npm run dev

# Or run compiled output (if you build to dist/)
node ./dist/cli.js --help
```

---

## ⚙️ Configuration

Create `tools/my-tool/.env` (or use your repo-standard config loader).

| Variable | Example | Purpose |
|---|---|---|
| `KFM_API_BASE_URL` | `http://localhost:8000` | Base URL for REST/GraphQL |
| `KFM_API_TOKEN` | `...` | Auth token for restricted endpoints |
| `KFM_PROFILE` | `dev` | Switches behavior per env |
| `KFM_OUTPUT_DIR` | `./out` | Output path for generated artifacts |

✅ Tip: prefer **explicit configuration** over “magic defaults” for reproducibility.

---

## 🗂️ Module map (suggested layout)

Keep modules small, composable, and **contract-shaped**:

```text
📁 src/
  📁 cli/                # arg parsing + command routing
  📁 commands/            # one folder per command
  📁 clients/             # REST/GraphQL wrappers
  📁 contracts/           # STAC/DCAT/PROV validation helpers
  📁 io/                  # filesystem + output formatting
  📁 logging/             # structured logs + verbosity
  📁 errors/              # typed errors + exit codes
  📄 index.ts             # library entry (optional)
```

---

## ➕ Add a new command

1. 📁 Create: `src/commands/<name>/`
2. Add “the trio”:
   - 📄 `schema.ts` — input validation
   - 📄 `handler.ts` — business logic (side-effect disciplined)
   - 📄 `examples.md` — copy/paste examples + expected output
3. 🔗 Wire it into `src/cli/` routing.
4. 🧪 Add tests + fixtures (“golden outputs” if generating artifacts).
5. 🧾 Ensure outputs include evidence pointers (dataset IDs, STAC/DCAT/PROV references).

---

## 🧪 Testing & quality gates

Recommended scripts:

```bash
npm run lint
npm run typecheck
npm test
```

### ✅ Definition of Done (DoD)
- ✅ Tests passing
- ✅ Docs updated (README + examples)
- ✅ Outputs trace to evidence
- ✅ No secret leakage (tokens never printed)
- ✅ Error paths return consistent exit codes

---

## 📦 Build & publish notes (if this becomes an npm package)

If you publish, generate a backwards-compatible build and automate it:

```json
{
  "scripts": {
    "build": "babel ./lib --out-dir ./dist-modules",
    "prepublish": "npm run build"
  }
}
```

Also consider ignoring build output in git:

```gitignore
dist-modules/
```

---

## 🧯 Troubleshooting

<details>
  <summary>Common issues (click to expand)</summary>

- **Port conflicts** 🔁  
  If `5432` / `8000` / `7474` are taken, update `docker-compose` port mappings.

- **Docker memory too low 🧠**  
  Large datasets/models need more RAM. Increase Docker’s memory allocation.

- **Auth failures 🔐**  
  Confirm `KFM_API_TOKEN` is set and that your role is permitted for ingest/pipeline endpoints.

- **Slow AI responses 🐢**  
  Verify your local LLM runtime (e.g., Ollama) is reachable and the model is pulled.

</details>

---

## 🔗 Related docs (within the repo)

- 📁 `docs/architecture/` — system design, AI integration, roadmap
- 📁 `docs/standards/` — contracts + documentation conventions
- 📁 `src/server/api/` — API docs (REST + GraphQL)
- 📁 `pipelines/` — ETL + reproducibility

---
