# Kansas Frontier Matrix (KFM) — `.github` 🧭🛡️

![Governed Docs](https://img.shields.io/badge/docs-governed-informational)
![Provenance-first](https://img.shields.io/badge/provenance-first-success)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)
![Policy-as-Code](https://img.shields.io/badge/policy-as--code-OPA-blue)
![Trust Membrane](https://img.shields.io/badge/trust--membrane-enforced-critical)
![Layer Coverage](https://img.shields.io/badge/layers-land%2Fwater%2Fgeo%2Fhazards%2Ftransport%2FAI-informational)

> [!IMPORTANT]
> This directory is part of KFM’s **trust membrane**: contributors and automation should enforce that clients never bypass governed APIs/policies to reach data stores directly.
> If you change what users can see (data layers, narratives, AI output), expect CI gates to require provenance, policy checks, and validation.

> [!NOTE]
> Some filenames and workflows below are **recommended defaults** and may differ in your repository. If a path is missing, treat it as **(not confirmed in repo)** and align it to the canonical standards in `docs/`.

---

## Table of contents

- [Why `.github` exists](#why-github-exists)
- [Directory layout](#directory-layout)
- [CI quality gates](#ci-quality-gates)
  - [Gate registry](#gate-registry)
  - [Layer integration and coverage gates](#layer-integration-and-coverage-gates)
  - [AI-driven experiments and “driving” workflows](#ai-driven-experiments-and-driving-workflows)
- [CI flow](#ci-flow)
- [Local preflight](#local-preflight)
- [Pull request checklist](#pull-request-checklist)
- [Governance and sensitive information](#governance-and-sensitive-information)
- [Key internal references](#key-internal-references)

---

## Why `.github` exists

KFM is an evidence-first, provenance-centric geospatial system:

**pipelines + catalogs + knowledge graph + governed API + map/timeline UI + Story Nodes + Focus Mode**

This directory operationalizes that stance in GitHub by housing:

- **CI workflows** (lint/validate/test/build gates)
- **Contribution UX** (issue forms, PR template, CODEOWNERS)
- **Security / policy entry points** (as applicable)

The goal: keep changes reviewable and safe-by-design—especially for provenance, governance, sensitive-location handling, and **layer coverage** across:

- **Land ownership / cadastral**
- **Historical events + historical figures**
- **Hydrology / water systems**
- **Geology / terrain**
- **Disasters / hazards**
- **Air quality + smoke**
- **Soils**
- **Fires**
- **Transportation: roads + rail/trains**
- **AI-driven experiments** (including remote-sensing extraction, routing/“driving distance”, and modeling workflows)

---

## Directory layout

> [!TIP]
> If you add new automation, prefer small, composable workflows with clear names and explicit “what/why” descriptions.
> If you already run these checks in fewer workflows (single “mega-workflow”), keep the **gate semantics** stable.

```text
.github/
  README.md                        # (this file) how GitHub automation enforces KFM gates
  workflows/
    docs.yml                       # docs lint + structure + link + accessibility + sensitivity
    data-catalog.yml               # STAC/DCAT/PROV validation + provenance checks
    layers.yml                     # geospatial layer QA (geometry/raster) + thematic layer coverage
    knowledge-graph.yml            # graph schema checks (events, figures, orgs) + provenance links
    hazards-env.yml                # disasters + fires + smoke/air-quality + water time-series checks
    transport.yml                  # roads + rail network integrity checks (topology, connectivity)
    ai-experiments.yml             # experiment manifests + reproducibility + model cards (fail closed)
    api-contracts.yml              # OpenAPI/GraphQL contract & compatibility checks
    policy.yml                     # OPA/Rego unit tests (+ “fail closed” posture checks)
    e2e.yml                        # UI + API end-to-end tests (provenance panel, citations)
    supply-chain.yml               # SBOM + provenance attestations (SLSA/in-toto)
  ISSUE_TEMPLATE/
    bug_report.yml
    feature_request.yml
    story_node.yml                 # optional: Story Node proposal intake
    layer_request.yml              # optional: new layer request intake (land/water/soil/etc.)
    experiment_report.yml          # optional: experiment proposal/results intake
  PULL_REQUEST_TEMPLATE.md
  CODEOWNERS
  dependabot.yml                   # optional
  SECURITY.md                      # optional
```

> [!NOTE]
> If `layers.yml` / `hazards-env.yml` / `transport.yml` / `ai-experiments.yml` don’t exist, **do not create “stub” workflows**.
> Instead, implement their checks as jobs inside existing workflows and update this README to reflect the final arrangement.

---

## CI quality gates

> [!WARNING]
> CI gates are not “nice to have” in KFM. Docs, data, policies, and experiments are governed artifacts:
> **a PR that weakens validation/provenance/sensitivity requirements is a governance change**.

### Gate registry

| Gate | What it checks | Why it exists | Typical implementation notes |
|---|---|---|---|
| Docs lint + structure | Markdown lint, heading order, template compliance | Prevents drift from governed templates; keeps docs machine-ingestible | Pair with link-check + accessibility |
| Provenance rules | “No claim without evidence,” references resolved | Supports cite-or-abstain behavior and auditability | Treat missing evidence as **blockers** |
| Link integrity | No broken internal links/images | Keeps docs renderable & CI-clean | Include relative-link checks |
| Accessibility | Alt text, table headers, heading hierarchy | Makes docs usable and reviewable | Fail on missing alt text for meaningful images |
| Sensitivity scanning | Flags sensitive content (precise locations, culturally restricted data) | Prevents unsafe exposure; protects community rights | Prefer redaction/generalization; add review flags |
| **Land/ownership governance** | Parcel/ownership fields reviewed; PII rules; license/terms checks | Land records can carry sensitive info and legal constraints | Default to aggregation/redaction; policy-gated fields[^pii] |
| Data catalog validation | STAC / DCAT v3 / PROV(-O) structure | Ensures interoperability and traceable lineage | Validate JSON + JSON-LD where applicable |
| **Layer QA (vector/raster)** | Geometry validity, CRS, bounds, nodata, tiling readiness | Prevents broken map layers and invalid analytics | Use GDAL/OGR + lightweight checks; fail fast |
| **Hydrology & water time-series QA** | Temporal schema, units, missingness, station metadata | Water layers are both spatial and temporal; errors mislead | Validate time windows + units; require provenance |
| **Geology & terrain QA** | Raster metadata, resolutions, hillshade/DEM consistency | Terrain layers underpin many derived analyses | Enforce CRS + pixel size + provenance |
| **Disaster & hazard QA** | Event integrity, geometry/time alignment, categorization | Timelines must remain queryable and explainable | Treat “unknown time/place” as explicit uncertainty |
| **Fire + smoke/air-quality QA** | Fire perimeters, smoke extents, AQ time series, linkage | Avoids inconsistent hazard narratives and maps | Require explicit source + update cadence notes |
| **Transport (roads/rail) QA** | Connectivity, topology, route break detection | Routing and “driving distance” analyses depend on topology | Add sanity checks: disconnected components, invalid lines |
| Knowledge graph validation | Graph schema (nodes/edges), IDs, backrefs to evidence | Keeps history/people/places joinable with sources | Validate ID conventions; require evidence links |
| API contract checks | OpenAPI diffs; consumer contract tests | Prevents breaking clients; keeps API governed | Require versioning + compatibility notes |
| Policy-as-code tests | OPA/Rego unit tests for allow/deny | Ensures governance gates behave predictably | Default-deny / fail-closed posture |
| End-to-end flows | UI provenance panel; Story Node citations; Focus Mode citation resolution | Ensures provenance UX works in practice | Treat “citation missing” as failure |
| Supply chain integrity | SBOM + provenance attestations | Hardens build integrity | Generate SPDX + SLSA/in-toto attestations |

---

### Layer integration and coverage gates

KFM treats “adding a layer” as **more than adding a file**. A “layer” is *integrated* only when it is:

1) processed/normalized,  
2) cataloged (STAC/DCAT) + provenance logged (PROV),  
3) stored via governed interfaces,  
4) exposed via governed API,  
5) policy-scoped, and  
6) visible in UI/Story Nodes with citations.

> [!IMPORTANT]
> Any PR that tries to “just drop a GeoJSON into the UI” (or bypass metadata/provenance) violates KFM’s pipeline–catalog–API invariant and should be blocked in CI.

#### Coverage matrix (themes → minimum CI expectations)

| Theme | Typical artifacts (examples; paths may vary) | CI must enforce | Governance notes |
|---|---|---|---|
| **Land ownership / cadastral** | parcels, grants/patents, plats | PII/sensitivity scan; schema validation; provenance required | Aggregate/redact owners/addresses by default[^pii] |
| **Historical figures** | person/org entity records linked to events/places | Evidence links required; disambiguation + stable IDs | Avoid doxxing; treat living persons with extra care |
| **Hydrology** | rivers/streams, watersheds, aquifers, gauges | Time-series QA + spatial QA; unit checks | Clearly label uncertainty and data gaps |
| **Geology / terrain** | DEM/hillshade/geo units | Raster QA (CRS/resolution/nodata); provenance | Derived products must cite inputs |
| **Disasters** | FEMA/NOAA-style events, impact footprints | Event schema + time/space coherence; provenance | “Unknown” fields must be explicit |
| **Air quality / smoke** | AQ sensors, smoke plumes, derived AQ maps | Time-series QA; smoke/AQ linkage tests; provenance | Communicate limitations/latency |
| **Soil** | soil surveys, soil moisture/erosion proxies | Schema + units; spatial QA | Respect licensing + attribution |
| **Fires** | incident perimeters, burn severity | Geometry/time QA; link to smoke/AQ where relevant | Do not publish sensitive tactical details |
| **Roads** | road network lines, classifications | Topology/connectivity checks; CRS | Routing outputs must be reproducible |
| **Rail / trains** | rail network lines, stations/yards | Topology/connectivity checks; CRS | Some assets may be security-sensitive |
| **AI-driven “driving” workflows** | experiment manifests, eval outputs | Reproducibility gates; model cards; data locks | No silent model changes; fail closed |

> [!TIP]
> You can enforce coverage by requiring a small **layer manifest** (recommended; not confirmed in repo) where every map-visible layer is declared with:
> - `layer_id`
> - `theme` (land/hydro/geo/hazards/air/soil/fire/transport)
> - dataset IDs (STAC/DCAT)
> - provenance IDs (PROV)
> - policy tags (OPA)
> - UI exposure flags

---

### AI-driven experiments and “driving” workflows

KFM explicitly supports AI-assisted analysis, but **only under governance**.

That includes experiments such as:

- Remote-sensing extraction of **roads/railways** and infrastructure features
- Spatiotemporal modeling of hazards (**fires**, **smoke**, **air quality**, **floods**, etc.)
- Graph-based analyses that can include “driving distance” style routing over road networks
- AI-assisted story drafting (must remain evidence-backed and reviewed)

#### What CI should require for experiments (recommended default)

> [!CAUTION]
> Experiments are not “just notebooks.” They can alter narratives, map layers, and public claims. Treat experiment outputs as governed artifacts.

Minimum expectations (paths are recommended; not confirmed in repo):

- `experiments/<id>/manifest.yaml`  
  - dataset IDs + exact versions (STAC/DCAT references)  
  - code revision reference (commit SHA)  
  - parameters + seeds  
  - intended use + limitations  
- `experiments/<id>/results/`  
  - metrics + evaluation summary  
  - artifacts with hashes (if applicable)  
- `mcp/model_cards/<model>.md` (or equivalent)  
  - what the model does/doesn’t do  
  - training/eval data provenance  
  - risks + bias notes  
- **Policy checks** (OPA) for:  
  - whether the output is allowed to ship to public UI  
  - whether it may reference sensitive locations/attributes  
  - whether it may be used by Focus Mode as a citation source

CI gating recommendations:

- Fail if an experiment references datasets without resolvable catalog/provenance IDs.
- Fail if results are missing **limitations** or **uncertainty** fields.
- Fail if a model is changed without updating its model card + evaluation summary.
- Fail closed by default: experiments don’t become “public layers” unless explicitly promoted via a governed step.

---

## CI flow

```mermaid
flowchart LR
  PR[Pull Request] --> Lint[Docs lint + structure\n+ links + a11y + sensitivity]
  PR --> Catalog[Data catalog validation\n(STAC/DCAT/PROV + provenance rules)]
  PR --> Layers[Layer QA\n(vector + raster + coverage)]
  PR --> KG[Knowledge graph checks\n(events + figures + IDs)]
  PR --> Haz[Hazards & environment\n(disaster/fire/smoke/AQ/water)]
  PR --> Trans[Transport QA\n(roads + rail topology)]
  PR --> Exp[AI experiment governance\n(manifest + eval + model cards)]
  PR --> Contracts[API contract checks\n(OpenAPI/GraphQL)]
  PR --> Policy[OPA policy tests\n(default deny / fail closed)]
  PR --> E2E[End-to-end flows\n(UI provenance + citations)]
  PR --> Supply[SBOM + provenance attestations]

  Lint --> Merge{Merge allowed?}
  Catalog --> Merge
  Layers --> Merge
  KG --> Merge
  Haz --> Merge
  Trans --> Merge
  Exp --> Merge
  Contracts --> Merge
  Policy --> Merge
  E2E --> Merge
  Supply --> Merge
```

---

## Local preflight

> [!TIP]
> Run local checks before you push. If the repo includes `pre-commit`, it’s usually the fastest “CI mirror.”

Recommended preflight sequence:

```bash
# 1) Run local hooks (if configured)
pre-commit run --all-files

# 2) Preview Markdown (GitHub / VSCode preview)
# 3) Verify links and references resolve
# 4) For non-trivial doc changes, update Version History (where required by the doc template)
```

If you are modifying pipelines, policies, layer data, or contracts, also run the relevant local test commands for those subsystems **(not confirmed in repo)**.

---

## Pull request checklist

- [ ] **Scope is declared** (docs / data / backend / web / policy / experiments)
- [ ] **Provenance included** for every substantive claim or new layer/story assertion
- [ ] **Layer coverage declared** (what theme? land/hydro/geo/hazards/air/soil/fire/transport)
- [ ] **Sensitive content reviewed**: precise locations redacted/generalized; review flags added
- [ ] **Land ownership reviewed** (PII/terms/licensing) if parcel/ownership-like fields appear
- [ ] **Hydrology/air/soil/fire/disaster** time-series or event integrity validated (units + time windows)
- [ ] **Roads/rail** topology sanity checked (connectivity / invalid geometries)
- [ ] **Historical figures** have stable IDs + evidence links (no “unsourced biography”)
- [ ] **Docs are template-aligned** (if using governed templates)
- [ ] **Policy impact assessed** (OPA rules updated + tests added where needed)
- [ ] **Contracts updated** (OpenAPI/GraphQL) with compatibility notes
- [ ] **Experiment governance satisfied** (manifest + eval + model card) if touching AI/ML
- [ ] **Validators and tests pass** locally (or explain why CI should be the source of truth)
- [ ] **No trust-membrane violations** (no direct DB access from UI/external clients)

---

## Governance and sensitive information

KFM is committed to:

- **FAIR** (Findable, Accessible, Interoperable, Reusable)
- **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics)

Practical implications for GitHub work:

- Treat docs/data/policies/experiments as **governed artifacts**, not “just text.”
- Avoid publishing **precise locations** of sacred/vulnerable sites.
- Avoid publishing **personal data** in land/ownership-like datasets (names, addresses, phone numbers, etc.). Prefer aggregation or redaction.[^pii]
- If content touches Indigenous histories or culturally restricted information, add an explicit **review trigger** in the PR description and route to governance reviewers **(process specifics may vary by repo)**.
- For hazards (fires/disasters), avoid operationally sensitive details (e.g., tactical response locations) unless explicitly cleared for release.

> [!IMPORTANT]
> When in doubt: **generalize, redact, and flag for governance review** rather than exposing details.

---

## Key internal references

All paths below are referenced by KFM’s documentation standards; if any are missing, treat them as **(not confirmed in repo)** and reconcile to the canonical layout.

- Docs standards:
  - `../docs/standards/KFM_MARKDOWN_WORK_PROTOCOL.md`
  - `../docs/standards/KFM_CHATGPT_WORK_PROTOCOL.md`
- Doc templates:
  - `../docs/templates/TEMPLATE__STORY_NODE_V3.md`
  - `../docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`
- Governance:
  - `../docs/governance/ROOT_GOVERNANCE.md`
  - `../docs/governance/ETHICS.md`
  - `../docs/governance/SOVEREIGNTY.md`
- Data catalog + provenance (recommended; not confirmed in repo):
  - `../data/catalog/` (STAC/DCAT)
  - `../data/provenance/` (PROV)
  - `../data/sources/` (source inventories; e.g., hydrology/terrain/etc.)
- Story Nodes (recommended; not confirmed in repo):
  - `../docs/stories/`
  - `../docs/stories/media/`
- AI + experiments (recommended; not confirmed in repo):
  - `../experiments/`
  - `../mcp/model_cards/`

---

<details>
  <summary>Maintainers: how to extend CI gates safely</summary>

- Prefer adding a **new job** to an existing workflow over creating many small workflows, *unless* the gate needs independent approvals.
- Any gate change that relaxes provenance/sensitivity requirements should be treated as a **governance change**:
  - document rationale
  - add tests
  - require review by governance owners (e.g., via CODEOWNERS)
- Keep workflow outputs legible:
  - write clear step names
  - attach artifacts (lint reports, schema validation logs) when failures are complex
- For new “layer themes” (e.g., adding a new hazard category):
  - update the **coverage matrix**
  - add policy tags + OPA tests
  - add at least one E2E scenario proving provenance and citations render correctly

</details>

---

[^pii]: Land/parcel ownership and related records can contain personally identifying information. In KFM, publishing such fields should be policy-gated by default (aggregate/redact), and any exposure should be reviewed as a governance decision.