# 🌐 External Adapters (Outbound Integrations)

![layer](https://img.shields.io/badge/layer-api%2Fadapters%2Fexternal-blue)
![architecture](https://img.shields.io/badge/architecture-clean%20%2F%20hexagonal-brightgreen)
![principle](https://img.shields.io/badge/principle-provenance--first-purple)
![goal](https://img.shields.io/badge/goal-avoid%20vendor%20lock--in-orange)

> **Purpose:** This folder holds **outbound adapters** that let KFM talk to **third‑party/external systems** (HTTP APIs, SaaS services, remote data providers, local model servers, etc.) while keeping **domain + service logic clean and testable**.  
> KFM’s architecture explicitly separates business logic from implementation details using adapters in `api/adapters/` as the bridge layer.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧭 What belongs here?

✅ **Good fits**
- 🌦️ **External HTTP APIs** (e.g., weather, geocoding, gazetteers, archival APIs)
- 🧠 **AI/LLM providers** (local or remote), including “tool-using” agent loops when applicable
- 🛰️ **Remote data services** (download/metadata fetchers, satellite catalog APIs, etc.)
- 🧾 **External metadata registries** (if KFM ever federates catalogs)

🚫 **Not a fit**
- Database adapters (those typically live under `api/db/` or a dedicated internal adapter folder)
- FastAPI route handlers (those are in `api/routes/` or equivalent)
- Core business logic / domain models (those belong in service/domain layers)

KFM uses a clean/hexagonal mindset: **business logic stays centered**, while adapters handle the messy world (HTTP protocols, auth, retries, vendor quirks).  [oai_citation:2‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:4‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

---

## 🧩 How this fits the overall architecture

```mermaid
flowchart LR
  A[🧠 Service / Use-Case Layer] -->|calls Port/Interface| B[🔌 Port (Protocol/ABC)]
  B -->|implemented by| C[🌐 External Adapter]
  C -->|HTTP / SDK / RPC| D[(☁️ External Service)]
  C -->|🧾 provenance + logs| E[(📜 audit trail)]
```

- **Service layer** depends on **ports/interfaces** (not concrete vendors).
- **External adapter** implements the port and owns:
  - HTTP requests, auth, retries, response parsing
  - vendor-specific quirks & error mapping
  - observability & provenance capture

This separation is aligned with KFM’s “integration layer” concept (interfaces & adapters under `api/db/` / `api/adapters/`).  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 📁 Suggested folder layout (conventional)

> Adjust to match the repo’s existing conventions—this is the “default good shape”.

```text
api/
  adapters/
    external/
      README.md

      _shared/                # ♻️ cross-adapter utilities (optional)
        http_client.py        # timeouts, retries, headers, tracing
        errors.py             # base error taxonomy + mapping helpers
        telemetry.py          # structured logs + timing helpers
        provenance.py         # provenance event writer (if shared)

      weather/                # 🌦️ example domain
        openweathermap_adapter.py
        models.py
        __init__.py

      geocoding/              # 🧭 example domain
        geocoding_service_adapter.py
        models.py
        __init__.py

      llm/                    # 🧠 local/remote model providers
        ollama_adapter.py
        models.py
        __init__.py
```

KFM blueprint examples explicitly call out external adapters like `OpenWeatherMapAdapter` and an external `GeocodingService`, including config management via env/config.  [oai_citation:6‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🧱 Adapter design rules (the “contract”)

### 1) Treat external calls as **volatile**
External services fail, throttle, change schemas, or return partial results. Build for it:
- ⏱️ timeouts (always)
- 🔁 retries with jittered backoff (only for safe/retriable errors)
- 🧯 circuit breaking / fail-fast (optional but recommended for hot paths)
- 🧊 caching (if safe & beneficial)
- 🧰 strict parsing & validation (e.g., Pydantic models)

### 2) Hide vendor specifics behind a **port**
- Define an interface in the service layer: `WeatherPort`, `GeocoderPort`, `LLMPort`, etc.
- The service calls the port; the adapter implements it.
- This supports swapping providers and helps **avoid vendor lock-in**—a key principle in data platform architecture.  [oai_citation:7‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

### 3) Normalize errors (don’t leak vendor exceptions)
External adapters should translate vendor/SDK exceptions into a small internal taxonomy, e.g.:
- `ExternalServiceTimeout`
- `ExternalServiceAuthError`
- `ExternalServiceRateLimited`
- `ExternalServiceBadResponse`
- `ExternalServiceUnavailable`

### 4) Config belongs in the adapter layer
Adapters manage secrets + endpoints via environment/config injection (never hardcode):
- `*_BASE_URL`
- `*_API_KEY`
- `*_TIMEOUT_SECONDS`
- `*_RETRY_MAX`

KFM blueprint notes adapters manage configuration like connection strings/URLs via env/config and keep credentials separate from business logic.  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 5) **Provenance-first** isn’t optional in KFM
If an adapter fetches data that ends up in:
- `data/processed/`
- the catalog/metadata
- user-facing answers (including AI outputs)

…then capture an auditable trace:
- who/what called the service (agent/service name)
- when (timestamp)
- what (endpoint + query parameters, redacting secrets)
- where from (provider + version if known)
- result identifiers (ETag/hash/record IDs)
- any transforms applied downstream

KFM’s provenance logs are designed to answer “How was this data produced?” with structured lineage metadata.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

---

## 🔐 Security baseline (practical + non-negotiable)

At minimum:
- 🔒 TLS for outbound calls where applicable
- 🔑 secrets never committed; redact in logs
- ✅ mutual auth/token auth where required
- 🧾 request/response logging with safe redaction
- 📌 stable audit trail (especially for data used in outputs)

Data-space security profiles emphasize secure communication (encryption + integrity), mutual authentication, access control, and logging as baseline expectations.  [oai_citation:10‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)

---

## 🧠 LLM / Agent adapters (special considerations)

KFM’s roadmap includes agentic multi-hop reasoning where an LLM can call *safe* backend tools (search docs, query data, etc.), and notes that models can be run locally via Ollama.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:12‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)

### 🦙 Ollama adapter notes
If you add an Ollama adapter, the Ollama HTTP API pattern shown in project materials uses `POST /api/generate` on the Ollama server.  [oai_citation:13‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)

Recommended adapter responsibilities:
- model selection + validation
- streaming vs non-streaming handling
- prompt templates (kept thin; heavy prompting belongs closer to service layer)
- tool-call/agent loop glue (if implemented here, keep it minimal and policy-guarded)
- provenance logs: model name/tag, prompt hash (not raw prompt if sensitive), tool calls, citations used

---

## 🧪 Testing strategy

### Unit tests (fast, deterministic)
- Mock HTTP responses (e.g., `respx`/`responses`/built-in mocking)
- Validate schema parsing
- Validate error mapping and retries
- Validate redaction rules

### Integration tests (optional but valuable)
- Run with Docker Compose dependencies (if present)
- Hit a sandbox/staging endpoint
- Use recorded fixtures for stable replay where possible

✅ **Rule of thumb:** if the service layer can be tested with a fake port, the adapter should be tested with a fake network.

---

## 🛠️ “Add a new adapter” checklist

- [ ] Define/confirm the **Port** interface in the service layer
- [ ] Create adapter module under `api/adapters/external/<domain>/`
- [ ] Add strict request/response models
- [ ] Add timeouts + retry policy
- [ ] Add error normalization
- [ ] Add structured logs + redaction
- [ ] Add provenance event(s) for any data used downstream
- [ ] Wire adapter via DI in API composition root (not inside the adapter)
- [ ] Unit tests (plus integration tests if high-impact)

---

## 📚 Project-grounded references

- KFM clean architecture explicitly places **interfaces & adapters** in the integration layer and calls out `api/adapters/` as a home for API adapters.  [oai_citation:14‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- KFM examples of external adapters: **OpenWeatherMapAdapter**, **GeocodingService**, and guidance that adapters handle configuration via env/config.  [oai_citation:15‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Hexagonal framing: inbound adapters call business logic; outbound adapters invoke external apps/services.  [oai_citation:16‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)
- Data platform principles include **security/privacy** and **avoiding vendor lock-in**.  [oai_citation:17‡Data Spaces.pdf](sediment://file_0000000053c071f5a9733b1b09cc9f76)
- Provenance logs are first-class artifacts intended to answer “How was this data produced?” in structured form.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- KFM’s agentic roadmap mentions local models via Ollama and safe backend tool APIs.  [oai_citation:19‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d) [oai_citation:20‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Blueprint.pdf](sediment://file_000000006dbc71f89a5094ce310a452d)
- Ollama API example uses `POST http://localhost:11434/api/generate`.  [oai_citation:21‡Comprehensive Guide to Ollama and Its Supported Open-Source LLMs.pdf](file-service://file-WLPhJVNoBxYKcy3utQSwBi)