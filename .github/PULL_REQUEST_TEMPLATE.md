<!--
Kansas Frontier Matrix (KFM) — Pull Request Template (vNext)

Canonical pipeline (non-negotiable ordering):
ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode

Hard review blockers (do not merge if violated):
1) UI reads via API only (no direct Neo4j/graph calls from web/**)
2) No unsourced narrative (Story Nodes + Focus Mode must be provenance-linked)
3) Contracts + schemas are versioned + validated (breaking changes require versioning + compat tests)
4) Pipelines write outputs under data/**; do NOT write derived catalogs/artifacts into docs/**

Minimum CI expectations (v12+ style gates; run what applies):
- Markdown protocol checks + link/reference checks
- Schema validation (STAC/DCAT/PROV/story nodes/ui/telemetry as applicable)
- Graph integrity tests (constraints, required relations, no orphans) when graph changes
- API contract tests when contracts changed
- Security/governance scanning: secrets/PII + sensitive-location leakage + classification propagation

Tip: Delete sections that clearly do not apply, but keep the “Core merge gate” checklist.
-->

## 📌 Summary
<!-- 1–5 sentences: what changed + why now -->

## 🧾 Evidence & identifiers (fill what applies)
<!-- The goal: reviewers can verify provenance + contracts without hunting. -->
- PROV bundle / activity / run ID(s): <!-- e.g., data/prov/<prov-bundle>.json OR run-id -->
- STAC Collection ID(s): <!-- e.g., stac:<collection-id> -->
- STAC Item ID(s): <!-- e.g., stac:<item-id-1>, stac:<item-id-2> -->
- DCAT Dataset ID(s): <!-- e.g., dcat:<dataset-id> -->
- Graph build/migration ID(s): <!-- e.g., graph:migration:<id> -->
- API endpoints touched: <!-- e.g., GET /v1/... -->
- Contract file(s) touched: <!-- e.g., src/server/contracts/... -->
- UI layer ID(s) / registry key(s): <!-- e.g., layer:<id> -->
- Story Node ID(s) + path(s): <!-- e.g., urn:kfm:story:..., docs/reports/story_nodes/... -->
- MCP run ID(s) / report path(s): <!-- e.g., mcp/runs/<run-id>/... -->

## 🔗 Related work
- Issue / ticket: <!-- e.g., Closes #123 -->
- Design / ADR / spec (if any):
- Data source / license register (if any):
- Reviewer routing (if known): <!-- e.g., @data-steward, @api-owner, @ui-owner, @governance -->

## 🧭 Scope

### Type of change (check all that apply)
- [ ] Data ingestion / refresh
- [ ] New dataset / evidence artifact
- [ ] Catalog metadata (STAC/DCAT/PROV)
- [ ] Graph / ontology / ingest fixtures
- [ ] API boundary / contracts
- [ ] UI / map layers / Focus Mode UX
- [ ] Story Node content
- [ ] MCP / analysis / model artifacts
- [ ] Schemas / validators
- [ ] Tests
- [ ] CI / tooling
- [ ] Docs / standards
- [ ] Release / packaging

### Pipeline stages impacted (check all that apply)
- [ ] ETL / pipelines (`src/pipelines/**`) → outputs in `data/**/{raw,work,processed}`
- [ ] Catalogs (`data/stac/**`, `data/catalog/dcat/**`, `data/prov/**`)
- [ ] Graph (`src/graph/**`, `data/graph/**`)
- [ ] API boundary (`src/server/**`, `src/server/contracts/**`) <!-- if legacy: note `src/api/**` -->
- [ ] UI (`web/**`)
- [ ] Story Nodes (`docs/reports/story_nodes/**`)
- [ ] Focus Mode behavior (provenance-linked only)
- [ ] Schemas (`schemas/**`)
- [ ] Tests (`tests/**`)
- [ ] Tooling/CI (`.github/**`, `tools/**`)
- [ ] Releases (`releases/**`)

### Change risk (pick one)
- [ ] Low (docs-only / non-functional refactor / cosmetics)
- [ ] Medium (new dataset, new layer, non-breaking contract/schema change)
- [ ] High (breaking contract/schema, ontology changes, sensitive content, security-related)

### Key paths touched (high level)
<!-- Keep this short; list top-level or “root-ish” paths. -->
- `...`

---

## ✅ Core merge gate checklist (do not skip)
- [ ] **Architecture boundary preserved:** UI consumes data through APIs/contracts (no direct graph/DB calls from `web/**`).
- [ ] **Sourced narrative preserved:** no uncited facts in published Story Nodes / Focus Mode outputs; provenance links exist.
- [ ] **Provenance-first order preserved:** evidence is cataloged (STAC/DCAT/PROV) before graph load, API serving, or narrative surfacing.
- [ ] **Contracts remain canonical:** schema/contract changes are versioned, validated, and tested (breaking changes include compat/deprecation notes).
- [ ] **Determinism + stable IDs:** pipelines are idempotent/reproducible; downstream IDs/keys remain stable (or migrations are documented).
- [ ] **Data-vs-code separation preserved:** pipelines write outputs under `data/**` (not `docs/**`); STAC/DCAT/PROV not written into `docs/**`.
- [ ] **Security hygiene:** no secrets/tokens/keys committed; no accidental PII.
- [ ] **Governance + sovereignty checks:** sensitive-location leakage + classification propagation checks addressed (or marked N/A with rationale).
- [ ] **Link/reference integrity:** no broken internal references (paths/IDs) introduced; artifacts referenced by ID resolve.

---

## 📦 Evidence, provenance, and contracts

<details>
<summary><strong>Data / ETL checklist</strong> (open if this PR touches <code>src/pipelines/**</code> or <code>data/**</code>)</summary>

### Data run metadata (recommended)
- Run ID / activity ID:
- Config snapshot / parameters (path or commit):
- Input sources (high level):
- Output datasets (high level):

### Checks
- [ ] Raw snapshots are treated as immutable (`data/**/raw/**`).
- [ ] Intermediate artifacts are reproducible (`data/**/work/**`).
- [ ] Processed outputs are deterministic + diffable (`data/**/processed/**`).
- [ ] IDs/keys used downstream are stable (no silent re-keying without a migration note).
- [ ] Geometry + temporal fields validated (where applicable).
- [ ] License + attribution captured (prefer DCAT + source register where used).
- [ ] If new/changed dataset: a PROV activity bundle exists (or is linked) under `data/prov/**`.

</details>

<details>
<summary><strong>Catalogs (STAC/DCAT/PROV) checklist</strong> (open if this PR touches catalog outputs)</summary>

### IDs (fill what applies)
- STAC Collection ID(s):
- STAC Item ID(s):
- DCAT Dataset ID(s):
- PROV bundle/activity ID(s):

### Checks
- [ ] STAC Collection + Item(s) updated under `data/stac/**`.
- [ ] DCAT dataset record updated under `data/catalog/dcat/**`.
- [ ] PROV bundle updated under `data/prov/**`.
- [ ] Artifacts validate against the relevant schemas in `schemas/**` (if present).
- [ ] No orphan references (IDs/refs resolve across STAC/DCAT/PROV and any graph mappings).
- [ ] Version lineage recorded (prefer “new version + links”; avoid in-place overwrites without lineage).
- [ ] License + distribution metadata present (DCAT) and matches source terms.

</details>

<details>
<summary><strong>Graph checklist</strong> (open if this PR touches <code>src/graph/**</code> or <code>data/graph/**</code>)</summary>

### Graph change summary
- New labels / relationships (if any):
- Ontology binding impact (if any):
- Migration ID / name (if any):

### Checks
- [ ] Graph ingest uses **processed** outputs + catalog/prov artifacts (no raw ingestion).
- [ ] Graph nodes reference STAC/DCAT/PROV identifiers where applicable.
- [ ] Constraints / tests updated (uniqueness, required relationships, no orphan domain nodes).
- [ ] Any new labels/relations align with the repo ontology bindings (no ad-hoc semantics).
- [ ] Rollback plan for graph schema/migration included (if applicable).

</details>

<details>
<summary><strong>API boundary checklist</strong> (open if this PR touches <code>src/server/**</code> / contracts)</summary>

### API surface summary
- Endpoint(s) touched:
- Contract file(s) touched:
- Compatibility: <!-- compatible / version bump / deprecation -->
- Redaction/generalization rules touched (if any):

### Checks
- [ ] Contract(s) updated in `src/server/contracts/**` (or legacy path noted in this PR).
- [ ] Backward compatibility assessed (compatible vs version bump vs deprecation).
- [ ] Contract tests updated/added and passing.
- [ ] Redaction/generalization rules are enforced at the API boundary (not in UI).
- [ ] Responses link back to provenance identifiers (STAC item IDs, DCAT IDs, PROV activity/run IDs) where relevant.
- [ ] No “ungoverned narrative” added to API responses (data + governed content only).

</details>

<details>
<summary><strong>UI / Focus Mode checklist</strong> (open if this PR touches <code>web/**</code>)</summary>

### UI impact summary
- View(s)/component(s) touched:
- Layer ID(s) / registry key(s) touched:
- A11y notes (if applicable):

### Checks
- [ ] UI reads only from API endpoints and/or catalog endpoints (no direct Neo4j calls).
- [ ] Layer registry changes validate against `schemas/ui/**` (if present).
- [ ] Focus Mode surfaces **provenance-linked** content only (no uncited narrative).
- [ ] If introducing any AI-assisted UI narrative: it is opt-in, clearly labeled, and includes uncertainty metadata.
- [ ] Performance considerations noted (hot paths, bundle size, map render cost).

</details>

<details>
<summary><strong>Story Nodes checklist</strong> (open if this PR touches <code>docs/reports/story_nodes/**</code>)</summary>

### Story Node inventory
- Story Node ID(s):
- File path(s):

### Checks
- [ ] Story Nodes follow `docs/templates/TEMPLATE__STORY_NODE_V3.md`.
- [ ] Every factual claim is source-linked (dataset/document IDs).
- [ ] Key entity references resolve (Place/Person/Event IDs exist or have creation tickets).
- [ ] Sensitivity/redaction compliance reviewed (generalization where required).
- [ ] If any AI-generated text is included: it is explicitly marked, opt-in (where surfaced), and includes uncertainty metadata.

</details>

<details>
<summary><strong>MCP / analysis / models checklist</strong> (open if this PR touches <code>mcp/**</code>)</summary>

### Run metadata
- Run ID:
- Manifest path:
- Evaluation / evidence links:

### Checks
- [ ] `mcp/runs/**` contains run manifests/logs/pointers (not duplicated provenance payloads).
- [ ] PROV is produced (or linked) under `data/prov/**` for meaningful runs.
- [ ] If a model changed: model card updated (intended use, limits, evaluation evidence).
- [ ] Experiment reports clearly label **fact vs inference vs hypothesis**.
- [ ] Governance review flagged if work touches culturally sensitive knowledge, restricted locations, protected personal data, or high-impact narrative generation.

</details>

---

## 🧪 Validation / tests run
<!-- Include commands and results. Use ~~~ fences per repo Markdown protocol. Replace examples with actual commands used. -->

~~~bash
# Paste the commands you ran (examples only):
# <data validator> ...
# <schema validator> ...
# <unit tests> ...
# <ui tests> ...
~~~

### Checks (mark what applies)
- [ ] Markdown protocol checks (front-matter/required sections where applicable)
- [ ] Link/reference checks (internal refs, artifact IDs, docs links)
- [ ] Schema validation (STAC/DCAT/PROV/story nodes/UI/telemetry as applicable)
- [ ] Graph integrity tests (constraints, required relations, no orphans) (if graph changed)
- [ ] API contract tests (if contracts changed)
- [ ] Unit/integration tests (if code changed)
- [ ] Secrets scan clean (no tokens/keys)
- [ ] PII scan clean (if data touched)
- [ ] Sensitive-location leakage check addressed (if applicable)
- [ ] Classification propagation check addressed (if applicable)

---

## ⚠️ Breaking change / migration notes (if applicable)
- What breaks?
- Who is impacted (ETL, catalogs, graph, API clients, UI)?
- Migration path / deprecation window:
- Version bump (schemas/contracts/docs) needed?
- Rollback plan:

---

## 🖼️ UI evidence (if applicable)
- Screenshots / screen recordings:
- Accessibility notes (keyboard nav, contrast, map interactions):
- Performance notes (bundle size, render hotspots):

---

## 🧩 Extension points (only if this PR adds net-new capability)
<!-- Mirrors KFM’s cross-subsystem extension checklist: Data, STAC, PROV, Graph, APIs, UI, Focus Mode, Telemetry. -->
- [ ] Data / ETL
- [ ] STAC
- [ ] PROV
- [ ] Graph
- [ ] APIs
- [ ] UI
- [ ] Focus Mode
- [ ] Telemetry

---

## 🧭 Reviewer notes
- Areas to focus review:
- Risk / rollback plan:
- Follow-ups / tickets created:
