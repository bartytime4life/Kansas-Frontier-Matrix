<!--
Kansas Frontier Matrix (KFM) — Pull Request Template

Canonical pipeline (non-negotiable ordering):
ETL → STAC/DCAT/PROV → Graph → API boundary → UI → Story Nodes → Focus Mode

Core invariants to preserve:
1) UI reads via API only (no direct Neo4j/graph access)
2) No unsourced narrative (Story Nodes + Focus Mode must be provenance-linked)
3) Canonical contracts + schemas are versioned and validated
4) Data-vs-code separation (pipelines write to data/**, not docs/**)

Tip: Delete sections that clearly do not apply, but keep the “Core merge gate” checklist.
-->

## 📌 Summary
<!-- 1–5 sentences: what changed + why now -->

## 🔗 Related work
- Issue / ticket: <!-- e.g., Closes #123 -->
- Design / ADR / spec (if any):
- Data source / license register (if any):

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

### Key paths touched (high level)
<!-- Keep this short; list top-level or “root-ish” paths. -->
- `...`

---

## ✅ Core merge gate checklist (do not skip)
- [ ] **Architecture boundary preserved:** UI consumes data through APIs/contracts (no direct graph/DB calls from `web/**`).
- [ ] **Sourced narrative preserved:** no uncited facts in published Story Nodes / Focus Mode outputs; provenance links exist.
- [ ] **Contracts remain canonical:** schema/contract changes are versioned, validated, and tested.
- [ ] **Data-vs-code separation preserved:** pipelines write outputs under `data/**` (not `docs/**`); STAC/DCAT/PROV do not get written into `docs/**`.
- [ ] **Security hygiene:** no secrets/tokens/keys committed; no accidental PII.
- [ ] **Sensitivity review done (if applicable):** restricted locations / culturally sensitive knowledge handled via generalization + redaction and appropriate review gates.

---

## 📦 Evidence, provenance, and contracts

<details>
<summary><strong>Data / ETL checklist</strong> (open if this PR touches <code>src/pipelines/**</code> or <code>data/**</code>)</summary>

- [ ] Raw snapshots are treated as immutable (`data/**/raw/**`).
- [ ] Intermediate artifacts are reproducible (`data/**/work/**`).
- [ ] Processed outputs are deterministic + diffable (`data/**/processed/**`).
- [ ] IDs/keys used downstream are stable (no silent re-keying without a migration note).
- [ ] Geometry + temporal fields validated (where applicable).
- [ ] If new/changed dataset: a PROV activity bundle exists (or is linked) under `data/prov/**`.

</details>

<details>
<summary><strong>Catalogs (STAC/DCAT/PROV) checklist</strong> (open if this PR touches catalog outputs)</summary>

- [ ] STAC Collection + Item(s) updated under `data/stac/**`.
- [ ] DCAT dataset record updated under `data/catalog/dcat/**`.
- [ ] PROV bundle updated under `data/prov/**`.
- [ ] Artifacts validate against the relevant schemas in `schemas/**` (if present).
- [ ] No orphan references (IDs/refs resolve across STAC/DCAT/PROV and any graph mappings).
- [ ] Version lineage recorded (prefer “new version + links”; avoid in-place overwrites without lineage).

</details>

<details>
<summary><strong>Graph checklist</strong> (open if this PR touches <code>src/graph/**</code> or <code>data/graph/**</code>)</summary>

- [ ] Graph ingest uses **processed** outputs + catalog/prov artifacts (no raw ingestion).
- [ ] Graph nodes reference STAC/DCAT/PROV identifiers where applicable.
- [ ] Constraints / tests updated (uniqueness, required relationships, no orphan domain nodes).
- [ ] Any new labels/relations align with the repo ontology bindings (no ad-hoc semantics).

</details>

<details>
<summary><strong>API boundary checklist</strong> (open if this PR touches <code>src/server/**</code> / contracts)</summary>

- [ ] Contract(s) updated in `src/server/contracts/**` (or legacy path noted in this PR).
- [ ] Backward compatibility assessed (compatible vs version bump vs deprecation).
- [ ] Contract tests updated/added and passing.
- [ ] Redaction/generalization rules are enforced at the API boundary (not in UI).
- [ ] Responses link back to provenance identifiers (STAC item IDs, DCAT IDs, PROV activity/run IDs) where relevant.

</details>

<details>
<summary><strong>UI / Focus Mode checklist</strong> (open if this PR touches <code>web/**</code>)</summary>

- [ ] UI reads only from API endpoints and/or catalog endpoints (no direct Neo4j calls).
- [ ] Layer registry changes validate against `schemas/ui/**` (if present).
- [ ] Focus Mode surfaces **provenance-linked** content only (no uncited narrative).
- [ ] If introducing any AI-assisted UI narrative: it is opt-in, clearly labeled, and includes uncertainty metadata.

</details>

<details>
<summary><strong>Story Nodes checklist</strong> (open if this PR touches <code>docs/reports/story_nodes/**</code>)</summary>

- [ ] Story Nodes follow `docs/templates/TEMPLATE__STORY_NODE_V3.md`.
- [ ] Every factual claim is source-linked (dataset/document IDs).
- [ ] Key entity references resolve (Place/Person/Event IDs exist or have creation tickets).
- [ ] Sensitivity/redaction compliance reviewed (generalization where required).
- [ ] If any AI-generated text is included: it is explicitly marked, opt-in (where surfaced), and includes uncertainty metadata.

</details>

<details>
<summary><strong>MCP / analysis / models checklist</strong> (open if this PR touches <code>mcp/**</code>)</summary>

- [ ] `mcp/runs/**` contains run manifests/logs/pointers (not duplicated provenance payloads).
- [ ] PROV is produced (or linked) under `data/prov/**` for meaningful runs.
- [ ] If a model changed: model card updated (intended use, limits, evaluation evidence).
- [ ] Experiment reports clearly label **fact vs inference vs hypothesis**.
- [ ] Governance review flagged if work touches culturally sensitive knowledge, restricted locations, protected personal data, or high-impact narrative generation.

</details>

---

## 🧪 Validation / tests run
<!-- Include commands and results. Use ~~~ fences per repo Markdown protocol. -->

~~~bash
# Paste the commands you ran (examples only):
# pytest -q
# npm test
# make validate
~~~

- [ ] Markdown protocol checks (front-matter/required sections where applicable)
- [ ] Schema validation (STAC/DCAT/PROV/story nodes/UI/telemetry as applicable)
- [ ] API contract tests (if contracts changed)
- [ ] Unit/integration tests (if code changed)
- [ ] Secrets scan clean (no tokens/keys)

---

## ⚠️ Breaking change / migration notes (if applicable)
- What breaks?
- Who is impacted (ETL, catalogs, graph, API clients, UI)?
- Migration path / deprecation window:
- Version bump (schemas/contracts/docs) needed?

---

## 🖼️ UI evidence (if applicable)
- Screenshots / screen recordings:
- Accessibility notes (keyboard nav, contrast, map interactions):
- Performance notes (bundle size, render hotspots):

---

## 🧭 Reviewer notes
- Areas to focus review:
- Risk / rollback plan:
- Follow-ups / tickets created:
