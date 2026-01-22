# 🧾 Dev Provenance Policy Pack (`dev_prov`) 🔗  
> **Path:** `mcp/dev_prov/policies/` → policy docs + patterns for **policy-as-code** enforcement in the Kansas Frontier Matrix ecosystem.

![Policy-as-Code](https://img.shields.io/badge/policy--as--code-OPA%20%2B%20Conftest-blue)
![Metadata](https://img.shields.io/badge/metadata-STAC%20%7C%20DCAT%20%7C%20PROV-informational)
![Governance](https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-purple)
![Supply%20Chain](https://img.shields.io/badge/supply%20chain-Sigstore%20%2F%20Cosign-yellow)
![Provenance](https://img.shields.io/badge/provenance-%E2%9B%93%20enforced-success)

---

## 🎯 Why this exists

KFM treats **data + metadata + provenance as a single “data contract”**: every dataset must carry structured fields like source, license, extent, and processing steps **before it can be accepted**—and “mystery layers” are not allowed. This contract-first approach is enforced with validators and CI checks so the system can generate attributions/citations automatically and keep provenance intact.  [oai_citation:0‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

KFM also standardizes its metadata stack with **STAC / DCAT / W3C PROV** (and aligns with **FAIR + CARE**) so the platform remains traceable, interoperable, and ethically governed.  [oai_citation:1‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

This docs folder exists to make those principles **actionable + enforceable** via a reusable policy layer.

---

## ✅ Non‑negotiables (the “policy spine”)

> **Fail closed**: if a check can’t be performed, the safe default is to block ingestion/merge—not to “let it slide.” Missing provenance is a CI failure.  [oai_citation:2‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

- **No provenance gaps**: derived outputs must carry lineage forward.  [oai_citation:3‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **Evidence-first narratives**: short “Pulse” narratives & Story Nodes still require provenance + evidence manifests users can drill into.  [oai_citation:4‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- **AI must cite or refuse**: Focus Mode outputs must include citations; if it can’t cite, it must refuse.  [oai_citation:5‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **UI must surface “the map behind the map”**: every visualization should be traceable to source data/metadata.  [oai_citation:6‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)
- **Humans and agents are treated equally**: automation cannot bypass rules. Agent PRs are never auto-merged; they require human review and respect policy gates.  [oai_citation:7‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧩 Where policies run

KFM uses **OPA (Rego) + Conftest** to enforce rules during CI (policy pack), and can also consult OPA at runtime for high-stakes decisions (example: check policy **before executing a Focus Mode answer**).  [oai_citation:8‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### Policy gate flow (CI + runtime)
```mermaid
flowchart LR
  PR[PR / Commit / Agent Plan] --> CI[CI Policy Gates<br/>Conftest + Rego]
  CI -->|PASS ✅| Merge[Merge / Promote]
  CI -->|DENY ⛔| Fix[Fix / Add missing metadata<br/>or request waiver]
  Merge --> Runtime[Runtime Policy Checks<br/>OPA (optional)]
  Runtime --> API[API / Exports / Focus Mode]
  API --> Ledger[Immutable Governance Ledger<br/>(append-only audit)]
```
Runtime checks + logging reinforce traceability and accountability.  [oai_citation:9‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:10‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

---

## 🧱 Policy domains (what we enforce)

### 1) 📦 Catalog & metadata completeness (STAC/DCAT/PROV)
KFM’s governance gates include schema validation, STAC/DCAT/PROV completeness, license presence, sensitivity classification, and provenance completeness.  [oai_citation:11‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

### 2) ⛓ Provenance-first publishing (no bypassing pipeline order)
The data intake policy pack includes explicit rules such as:

- **Pipeline ordering**: later-stage artifacts must not appear without earlier-stage outputs (e.g., graph/UI references can’t “jump ahead” of catalogs/provenance).  [oai_citation:12‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **API boundary**: UI/code must not access the DB/graph directly; policy can detect “forbidden” paths/clients and fail PRs.  [oai_citation:13‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **Provenance-first publishing**: any change to processed data/graph/content must ship corresponding updates in `data/prov/` (and typically STAC/DCAT).  [oai_citation:14‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### 3) 🧑‍💻 `dev_prov`: DevOps → PROV graph integration
KFM maps GitHub PR activity to W3C PROV-O, generating JSON‑LD where PRs are **PROV Activities**, commits are **Entities**, and authors/reviewers are **Agents**—then ingesting those records into Neo4j so development history becomes queryable provenance.  [oai_citation:15‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

This allows invariant enforcement in CI (example: fail if merge commit nodes/relationships are missing or malformed).  [oai_citation:16‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### 4) 🤖 AI governance (Focus Mode + explainability + audit trail)
- **Immutable governance ledger** logs AI outputs and key decisions with compliance metadata.  [oai_citation:17‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **User-visible provenance**: UI supports “Layer Provenance” panels + export attributions and auto-generated citations on AI narratives.  [oai_citation:18‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Explainable AI** can expose an audit panel showing what influenced an answer and any governance flags (e.g., sensitive data notices).  [oai_citation:19‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)
- **Bias + drift monitoring** are part of QA; governance policies define content rules and escalation paths.  [oai_citation:20‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)

### 5) 🧬 Sensitive data & sovereignty controls
KFM supports sensitivity tagging, coordinate generalization, access control, and explicit permission requirements for precise culturally sensitive locations.  [oai_citation:21‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)

The “Innovative Concepts” research specifically calls out community-governed access models (e.g., Mukurtu-style cultural protocols) and differential access, with practical examples like geo-obfuscation/rounding for sensitive records.  [oai_citation:22‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)

> 🔐 **Policy implication:** policies should ensure **classification propagates** from ingestion → API → UI, so restricted layers either (a) don’t render, or (b) render in a generalized form.

### 6) 🔏 Supply chain & artifact integrity (OCI + signing)
KFM proposes provenance-first artifact storage using OCI registries, leveraging cosign/oras, and attaching provenance artifacts (PROV JSON‑LD, attestations) to binaries/tilesets so artifacts carry a certificate of origin.  [oai_citation:23‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### 7) 🩺 Graph integrity “unit tests” (health checks)
A weekly graph health check routine treats the knowledge graph like code—running validations for schema drift, constraint/index integrity, orphaned metadata, and ingestion anomalies.  [oai_citation:24‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

It explicitly targets broken lineage cases (example: PROV Activities without `:USED` / `:WAS_GENERATED_BY` edges).  [oai_citation:25‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🗂 Expected layout (recommended)

> This repo has historically referenced policy locations like `tools/validation/policy/` and `api/scripts/policy/`. This `mcp/dev_prov/policies/` tree can **vendor / mirror / bundle** the same policy logic in an MCP-friendly structure.  [oai_citation:26‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:27‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

```text
mcp/dev_prov/policies/
├─ docs/                          📚 docs (you are here)
│  └─ README.md                   ✅ policy overview + how-to
├─ rego/                          🧠 Rego policies (OPA)
│  ├─ catalog/                    📦 STAC/DCAT contract checks
│  ├─ prov/                       ⛓ provenance rules
│  ├─ dev_prov/                   🧑‍💻 PR→PROV invariants
│  ├─ ai/                         🤖 AI governance gates
│  ├─ security/                   🔐 secret scanning, pinned digests, etc.
│  └─ graph/                      🩺 graph health checks
├─ tests/                         ✅ policy tests (opa test)
├─ data/                          🧪 sample inputs (changed_files, manifests, etc.)
├─ bundles/                       📦 built OPA bundles (optional)
└─ waivers/                       🧾 time‑boxed exceptions (human-approved)
```

---

## 🚀 Quickstart (local)

### 1) Run policy checks like CI
> CI uses Conftest to evaluate Rego policies against repo state and changed files.  [oai_citation:28‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC) [oai_citation:29‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

```bash
# from repo root
conftest test \
  --policy mcp/dev_prov/policies/rego \
  --all-namespaces \
  data/
```

### 2) Run OPA unit tests
```bash
opa test -v mcp/dev_prov/policies/rego mcp/dev_prov/policies/tests
```

---

## 🧾 Policy IDs, severities, and messages

KFM policy gates are designed to fail with explicit, stable identifiers (example message shown in docs):  
- `KFM-PROV-001: Processed data changed without matching PROV update.`  [oai_citation:30‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

### Recommended ID scheme
| Prefix | Domain | Examples |
|---|---|---|
| `KFM-CAT-###` | Catalog + metadata contract | license, provider, contact, schema |
| `KFM-PROV-###` | Provenance chain | missing PROV, missing lineage edges |
| `KFM-DEVPROV-###` | Dev provenance | PR→PROV record missing, invariants broken |
| `KFM-AI-###` | AI governance | missing citations, restricted content |
| `KFM-SEC-###` | Security | secrets, unsigned artifacts, unpinned digests |
| `KFM-GRAPH-###` | Graph health | orphan nodes, constraints offline |

---

## ✍️ Authoring Rego policies (house rules)

### Style rules (recommended)
- **One policy file = one domain** (e.g., `prov/provenance_first.rego`).
- Prefer **`deny[msg]`** rules with stable IDs and actionable messages.
- Keep policies **data-driven** (vocabularies/allowlists belong in `data/`).

### Example: provenance-first publishing (simplified)
> The docs describe a “provenance-first publishing rule” that checks changed files and denies if processed outputs change without corresponding provenance updates.  [oai_citation:31‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

```rego
package kfm.prov

deny[msg] {
  some f
  f := input.changed_files[_]
  startswith(f, "data/processed/")
  not has_matching_prov(f)
  msg := sprintf("KFM-PROV-001: %s changed without matching PROV update.", [f])
}

has_matching_prov(f) {
  # Example mapping strategy: "data/processed/x.csv" -> "data/prov/x_prov.json"
  prov_path := replace(f, "data/processed/", "data/prov/")
  prov_path := sprintf("%s_prov.json", [trim_suffix(prov_path, ".csv")])
  prov_path == input.repo_files[_]
}
```

---

## 🧑‍💻 `dev_prov` specifics: PR → PROV JSON‑LD

KFM’s PR provenance mapping includes:
- PR as **PROV Activity**
- Commits as **PROV Entities**
- Authors/reviewers/CI bot as **PROV Agents**
- Relations like `prov:used`, `prov:wasAssociatedWith`, `prov:wasGeneratedBy`  [oai_citation:32‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

### Example JSON‑LD skeleton (illustrative)
```json
{
  "@context": "https://www.w3.org/ns/prov",
  "@id": "kfm:pr/1234",
  "@type": "prov:Activity",
  "prov:used": [{"@id": "kfm:commit/abcd"}],
  "prov:wasAssociatedWith": [{"@id": "kfm:agent/alice"}],
  "prov:generated": [{"@id": "kfm:commit/merge-efgh"}]
}
```

### Invariants worth gating (recommended)
- If PR is merged, **merge commit entity exists**
- Merge commit is **derived from expected source commits**
- PR provenance record is present for each state transition you care about  
These invariants are explicitly called out as enforceable in CI.  [oai_citation:33‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🧾 Run manifests & reproducibility (policy inputs)

A structured **Run Manifest** is saved per pipeline run (example location: `data/audits/<run_id>/run_manifest.json`) and can be used as a policy artifact.  [oai_citation:34‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

Key ideas:
- Manifest includes source URLs, tool versions, and record counts/errors.  [oai_citation:35‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Manifest JSON is canonicalized (RFC 8785) and hashed (SHA‑256) to produce a stable digest / idempotency key.  [oai_citation:36‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)
- Digest can be referenced in PROV records to uniquely identify activities.  [oai_citation:37‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

### Policy hooks to consider
- Deny if manifest missing required fields (source URLs, tool versions, counts).
- Deny if data changed but manifest digest not updated.
- Require manifest existence for “promotion” workflows.

---

## 🏗 CI/CD promotion + lineage events

KFM proposes a Detect → Validate → Promote workflow, where changes are validated and then promoted via a signed PR; lineage events (OpenLineage) are emitted with stable run identifiers for audit.  [oai_citation:38‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)

---

## 🔐 Agents, parity, and kill-switches

Key guardrails:
- Agent PRs are **never auto-merged**; they require human review.  [oai_citation:39‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Policies apply equally to humans and agents (“no bypass”).  [oai_citation:40‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- Kill-switch can halt agent-driven automation (e.g., a global flag or `.agent-freeze` pattern).  [oai_citation:41‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🩺 Graph health checks (turning the graph into a tested artifact)

The “Weekly Graph Health Check” idea includes:
- node/relationship delta checks,
- constraint/index status checks,
- orphaned metadata and broken lineage link checks.  [oai_citation:42‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

These checks can be scheduled in CI and version-controlled as part of the repo’s knowledge base.  [oai_citation:43‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)

---

## 🗺 UI integration: making policy visible (not just enforced)

The UI is designed for transparency: users should always be able to trace “the map behind the map,” and provenance/credits should surface in layers and exports.  [oai_citation:44‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt) [oai_citation:45‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)

Practical enforcement example (streaming/real-time):
- if a station is marked sensitive, the API can omit it or restrict it to authorized users; provenance is still logged and policies still apply.  [oai_citation:46‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)

---

## 🧠 Privacy & inference controls (policy inspiration)

Research notes in the project library highlight:
- messy/incorrect data undermines analysis and decision-making, motivating strong validation gates.  [oai_citation:47‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)
- query auditing and inference control can deny queries that risk disclosure of confidential data (and differential privacy can protect record-level privacy).  [oai_citation:48‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)

> 🧷 **Policy direction:** add “inference risk” policies for exports, aggregations, and repeated queries on sensitive layers.

---

## 🧭 Glossary (minimal)

- **PROV (W3C PROV-O)**: Entities (inputs/outputs), Activities (process), Agents (people/software); relations like `prov:used`, `prov:wasGeneratedBy`, `prov:wasAssociatedWith`.  [oai_citation:49‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
- **STAC / DCAT**: catalog standards used to describe datasets/assets at multiple levels; paired with PROV for lineage.  [oai_citation:50‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- **OPA / Rego / Conftest**: policy engine + language + CI runner used for policy gates.  [oai_citation:51‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)

---

## 🧰 MCP alignment notes (why this is under `mcp/`)

The KFM design research explicitly references MCP tool recommendations (QGIS/GDAL/Python for reproducibility) and highlights the importance of model metadata (model cards) for transparency.  [oai_citation:52‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)

This `mcp/dev_prov/policies/` package is designed to keep policy docs + artifacts:
- **reproducible** (run manifests, tests, fixtures),
- **inspectable** (policy rules are explicit, versioned),
- **portable** (bundle-able for CI and runtime).

---

## 📎 Source docs used (project files)

### Core KFM system docs
- Kansas Frontier Matrix – Comprehensive UI System Overview  [oai_citation:53‡Kansas Frontier Matrix – Comprehensive UI System Overview.pdf](file-service://file-KcBQruYcoFVDEixzzRHTwt)  
- 📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide  [oai_citation:54‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)  
- Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM)  [oai_citation:55‡Innovative Concepts to Evolve the Kansas Frontier Matrix (KFM).pdf](file-service://file-G71zNoWKxsoSW44iwZaaCC)  
- Additional Project Ideas  [oai_citation:56‡Additional Project Ideas.pdf](file-service://file-Pc2GNivcrHBeKjBQksLC3T)  

### Additional references (also used)
- Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation  [oai_citation:57‡Kansas Frontier Matrix (KFM) – Comprehensive Technical Documentation.pdf](file-service://file-AkqwUuYPp5zePf7pv5SMxi)  
- Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design  [oai_citation:58‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)  
- Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖  [oai_citation:59‡Kansas Frontier Matrix (KFM) – AI System Overview 🧭🤖.pdf](file-service://file-Pv8eev6RWvCKrGCXyzY7zg)  
- 🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals  [oai_citation:60‡🌟 Kansas Frontier Matrix – Latest Ideas & Future Proposals.docx.pdf](file-service://file-SQ3f7ve8SGiusT6ThZEuCe)  
- Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design  [oai_citation:61‡Kansas-Frontier-Matrix_ Open-Source Geospatial Historical Mapping Hub Design.pdf](file-service://file-ShqHKgjxCS9UT9vbcxDNzA)  
- Data Mining Concepts & applictions  [oai_citation:62‡Data Mining Concepts & applictions.pdf](file-service://file-2uwEbQAFVKpXaTtWgUirAH)  

### Project library “PDF portfolios” (present, but require extraction to read contents)
These are uploaded as PDF portfolios (Acrobat prompts show up during parsing):  
- AI Concepts & more  [oai_citation:63‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)  [oai_citation:64‡AI Concepts & more.pdf](file-service://file-K6BctJjeUwvyCahLf9qdwr)
- Maps / GoogleMaps / Virtual Worlds / WebGL  [oai_citation:65‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)  [oai_citation:66‡Maps-GoogleMaps-VirtualWorlds-Archaeological-Computer Graphics-Geospatial-webgl.pdf](file-service://file-RshcX5sNY2wpiNjRfoP6z6)
- Various programming languages & resources  [oai_citation:67‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)  [oai_citation:68‡Various programming langurages & resources 1.pdf](file-service://file-4wp3wSSZs7gk5qHWaJVudi)
- Data management / Bayesian methods / programming ideas  [oai_citation:69‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)  [oai_citation:70‡Data Managment-Theories-Architures-Data Science-Baysian Methods-Some Programming Ideas.pdf](file-service://file-RrXMFY7cP925exsQYermf2)

---

## ✅ Next actions (recommended)
- [ ] Mirror or link existing policy packs (e.g., `api/scripts/policy/` or `tools/validation/policy/`) into `mcp/dev_prov/policies/rego/`.  [oai_citation:71‡Kansas Frontier Matrix (KFM) – Comprehensive Architecture, Features, and Design.pdf](file-service://file-4Umt1yHoGKicdmLWzFJ9sC)
- [ ] Add fixtures for: `changed_files`, PR provenance JSON‑LD, run manifests, and graph snapshots.
- [ ] Add a “waiver” mechanism that is time-boxed + requires explicit approval (so “fail closed” remains the default).  [oai_citation:72‡📚 Kansas Frontier Matrix (KFM) Data Intake – Technical & Design Guide.pdf](file-service://file-EbUCdsJMbu5KwpoKMrLrgj)
