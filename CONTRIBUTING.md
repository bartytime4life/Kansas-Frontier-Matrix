# Contributing to Kansas Frontier Matrix (KFM)

> **KFM is an evidence-first Kansas story engine**: maps + timelines + narratives + auditable AI answers.  
> If you like building systems that *prove what they claim*, you’re in the right place.

Thank you for contributing. KFM is designed so that **every map layer, story claim, and Focus Mode answer can be traced back to primary evidence and transformation history**—not vibes. Your PR can improve how Kansas is understood and explored, *without sacrificing credibility*.  

---

## Table of contents

- [How to help (pick a path)](#how-to-help-pick-a-path)
- [KFM’s non-negotiables](#kfms-non-negotiables)
- [Repo layout](#repo-layout)
- [Local development quickstart](#local-development-quickstart)
- [Contribution workflow](#contribution-workflow)
- [What “governed” means here](#what-governed-means-here)
- [Contributing Story Nodes and docs](#contributing-story-nodes-and-docs)
- [Contributing data + pipelines](#contributing-data--pipelines)
- [Contributing API, backend, and UI](#contributing-api-backend-and-ui)
- [Contributing policy (OPA/Rego)](#contributing-policy-oparego)
- [Handling sensitive data (FAIR/CARE)](#handling-sensitive-data-faircare)
- [PR checklist](#pr-checklist)
- [Review process](#review-process)

---

## How to help (pick a path)

Choose what you want to ship. Each path has a checklist and “definition of done.”

### 🌾 Story + documentation (great first contributions)
- Fix clarity, add missing citations, improve explainers
- Author a Story Node step that ties **text → map state → evidence**

➡️ Start here: [Contributing Story Nodes and docs](#contributing-story-nodes-and-docs)

### 🧭 Data + pipelines (high impact)
- Add a new dataset integration
- Improve validation gates, catalogs (STAC/DCAT/PROV), or run records
- Strengthen reproducibility and provenance

➡️ Start here: [Contributing data + pipelines](#contributing-data--pipelines)

### 🧱 Backend/API/UI (make the experience sing)
- Improve provenance UX, evidence resolution, search/graph retrieval
- Make Focus Mode safer, more auditable, more deterministic
- Improve map performance and layer exploration

➡️ Start here: [Contributing API, backend, and UI](#contributing-api-backend-and-ui)

### 🛡️ Policy (make governance enforceable)
- Improve OPA rules + tests
- Add regression cases that prevent future leaks forever

➡️ Start here: [Contributing policy (OPA/Rego)](#contributing-policy-oparego)

---

## KFM’s non-negotiables

These are the “credibility contracts” of KFM. If a change violates one, it will be rejected.

> [!IMPORTANT]
> **Trust membrane:** Frontend and external clients never talk to databases directly. All access goes through the governed API + policy boundary.  
> **Fail-closed:** If the policy engine can’t decide, access is denied.  
> **Promotion gates:** No dataset is promoted/public without STAC/DCAT/PROV + checksums + validation.  
> **Focus Mode:** Must provide citations **or abstain**, and must return an audit reference.

---

## Repo layout

The repo is designed so code, data, and documentation evolve together and remain auditable.

```text
.github/     CI workflows (governance gates)
data/        raw/ work/ processed + catalogs (DCAT/STAC/PROV) + checksums
docs/        governed documentation + Story Nodes (validated)
policy/      OPA/Rego modules + unit tests (default deny)
src/         backend in clean layers (domain / usecases / adapters / infrastructure)
web/         React/TypeScript + Map UI (no direct DB access)
```

> [!NOTE]
> If your checkout differs, follow the repo as source-of-truth and submit a PR to update this file.

---

## Local development quickstart

KFM’s documented local workflow uses Docker Compose.

```bash
cp .env.example .env
docker compose up --build
```

Typical dev endpoints (documented):
- UI: `http://localhost:3000`
- API docs: `http://localhost:8000/docs`

Sanity check (smoke test idea):
- Load the home map
- Toggle a layer
- Open the provenance panel
- Run one Focus Mode query

> [!TIP]
> If Docker Compose isn’t available in your environment, contribute via docs/Story Nodes first—no local stack required.

---

## Contribution workflow

### 1) Pick scope
- **Small & reversible** beats big & risky.
- If you’re changing contracts/policy/data schemas, open an issue first.

### 2) Create a branch
```bash
git checkout -b feat/<short-topic>
# or
git checkout -b fix/<short-topic>
```

### 3) Make the change
- Keep commits focused.
- Add tests or validation artifacts as required.

### 4) Run checks locally (when applicable)
- Lint / format
- Unit tests
- Validators (Story Node / catalogs / policy)

### 5) Open a Pull Request
Your PR description should answer:
- **What changed?**
- **Why is it correct?**
- **What evidence/provenance did you add or preserve?**
- **How did you test it?**
- **Any sensitivity implications?**

---

## What “governed” means here

Some artifacts in KFM are **governed**: they are validated in CI and affect system credibility.

Governed artifacts commonly include:
- Story Nodes and governed Markdown docs
- Dataset catalogs (DCAT/STAC/PROV) and checksums
- OPA/Rego policy modules + tests
- OpenAPI contracts (and compatibility gates)
- Validators and promotion gates
- Audit/provenance formats and evidence resolver behavior

> [!IMPORTANT]
> **CI is part of governance.** If governed artifacts fail validation, the PR should fail.

---

## Contributing Story Nodes and docs

Story Nodes are **governed narrative units** authored in Markdown under a strict template (v3) and validated in CI. Every factual claim needs citations, and citations must resolve.  

### What to change/add
Common files:
- `docs/stories/<story-id>.md` (story text + citations)
- `docs/stories/<story-id>.json` (map/time “view state” actions; naming may vary)
- `docs/stories/media/...` (images/figures if used)

### Story Node expectations
A strong Story Node:
- Uses the v3 template (required sections: overview + titled steps)
- References datasets/layers by stable IDs
- Includes citations for factual statements
- Avoids sensitive location leakage (see [Handling sensitive data](#handling-sensitive-data-faircare))
- Passes the story validator (locally if available, always in CI)

> [!TIP]
> Think “interactive documentary”: each step can align narrative + time + geography + layers.

### Documentation PRs
For non-story docs:
- Prefer short sections with clear headings
- Add examples and verification steps
- Avoid stating uncertainty as fact (say what’s known, what’s assumed, and how to verify)

---

## Contributing data + pipelines

KFM treats each integrated source as a **governed Dataset** with explicit versioning:
- each ingest run produces a DatasetVersion (checksums + run metadata)
- catalogs emitted/updated (DCAT always; STAC/PROV as applicable)
- provenance links raw assets → processed derivatives
- policy labels and redactions are enforced

### Ingestion workflow shape
Most sources follow:
1. Discover (capabilities, parameters, auth)
2. Acquire (incremental slices when possible, else snapshot+diff)
3. Normalize (UTF‑8, WGS84, ISO 8601)
4. Validate (schema, geometry, temporal, license/policy)
5. Enrich (GeoIDs, joins, entity resolution candidates)
6. Publish (promote to processed, update catalogs, refresh indexes)

### Promotion gate checklist (required)
To promote to processed/public:
- license present
- sensitivity classification present
- schema + geospatial checks pass
- checksums computed
- STAC/DCAT/PROV exist and validate
- audit event recorded
- human approval if sensitive

### Run records (strongly recommended)
Each pipeline job should emit:
- `run_record.json` (inputs, code git sha/image, outputs, checksums refs)
- validation report
- provenance reference (PROV)

> [!IMPORTANT]
> “Processed” is the only publishable source of truth. Don’t serve raw/work intermediates to users.

### Test plan expectations (CI-ready)
A solid data PR often includes:
- Unit tests for schema mapping / coercion
- Integration test against a fixed small slice (stable checksums + counts)
- Contract tests verifying API response includes provenance bundle and respects redaction
- Regression/profiling checks (null rates, distributions) are stable or versioned

---

## Contributing API, backend, and UI

### Trust membrane rules (enforced)
- Frontend never calls DBs directly
- Policy evaluation occurs on every data/story/AI request
- Backend logic uses repository interfaces (ports); do not bypass them
- Audit and provenance are produced in the normal request path

### Clean layers contract (backend)
Backend layout is expected to follow clean layers:
- **Domain:** entities/value objects + invariants (pure unit tests)
- **Use Cases:** workflows + business rules (use-case tests with mocked ports)
- **Integration:** ports/contracts + DTOs (contract/schema tests)
- **Infrastructure:** DB clients, API handlers, OPA adapters (integration tests + E2E smoke tests)

### Contract-first API changes
If you change API behavior:
- update OpenAPI (treat it as governed)
- add contract tests
- avoid breaking changes for stable endpoints (e.g., `/api/v1/...`)

### Focus Mode expectations (when you touch AI/Q&A)
Focus Mode is constrained and auditable:
- retrieval should assemble an explicit evidence pack
- model drafts answer **without external browsing**
- policy validates: citations exist, sensitivity ok
- system appends audit event and returns `{ answer_markdown, citations[], audit_ref }`
- if evidence is insufficient, return an abstain response with `audit_ref`

> [!NOTE]
> Evidence/citation references must be resolvable to a human-readable “review evidence” view.

---

## Contributing policy (OPA/Rego)

Policy is how governance becomes enforceable.

### Baselines
- Default deny
- Require citations + sensitivity_ok for Focus Mode answers
- Fail closed when policy input is missing/invalid (don’t guess)

### What good looks like
- Add unit tests for allow/deny cases
- Add regression tests for any previously discovered leak
- Add negative tests for sensitive-location precision / restricted field exposure
- Ensure every API response includes an audit reference (integrity checks)

> [!IMPORTANT]
> Policies should prevent a bad outcome even if an upstream service behaves unexpectedly.

---

## Handling sensitive data (FAIR/CARE)

KFM explicitly treats some classes of data as sensitive (examples include private ownership records, precise archaeological site locations, and certain health/public-safety indicators).

### Sensitivity classes (common patterns)
- **Public:** safe to publish without redaction
- **Restricted:** requires role-based access (e.g., parcel ownership)
- **Sensitive-location:** coordinates must be generalized or suppressed (e.g., archaeology, sensitive species)
- **Aggregate-only:** publish only above thresholds (e.g., small counts)

### Redaction is a first-class transformation
- Raw datasets remain immutable
- Redacted derivatives are separate DatasetVersions (often separate dataset_id)
- Redaction must be recorded in provenance (PROV)
- CI should include non-regression tests to prevent leaks from returning

> [!CAUTION]
> Never paste restricted fields or precise sensitive coordinates into GitHub issues, PR descriptions, logs, screenshots, or test fixtures.

---

## PR checklist

Use this as your “ready to review” bar.

### Required (all PRs)
- [ ] The change is scoped and reviewable
- [ ] No direct DB access from frontend code
- [ ] Policy checks are not bypassed
- [ ] Tests/validators updated as needed
- [ ] Documentation updated if behavior changed

### If you touched Story Nodes/docs
- [ ] Story template requirements satisfied (overview + steps)
- [ ] Every factual claim has a citation
- [ ] Citations resolve (locators/snippets available via evidence tooling)
- [ ] No sensitive location leakage

### If you touched data/pipelines
- [ ] License recorded
- [ ] Sensitivity classified
- [ ] Validation gates pass (schema/geo/time)
- [ ] Checksums computed
- [ ] STAC/DCAT/PROV emitted and validated
- [ ] Audit event recorded (as applicable)
- [ ] Human approval path documented if sensitive
- [ ] Test plan included (unit/integration/contract/regression)

### If you touched policy
- [ ] Default deny preserved
- [ ] Unit tests for allow/deny behavior included
- [ ] Regression tests added for any leak/edge case

### If you touched API contracts
- [ ] OpenAPI updated (governed)
- [ ] Contract tests updated/added
- [ ] No breaking changes (or a version bump + migration plan)

---

## Review process

Most PRs are reviewed by maintainers; subject-matter experts may be pulled in for:
- historical accuracy
- citation quality and provenance clarity
- sensitive content review (especially for culturally restricted knowledge or precise locations)

When your PR merges:
- governed docs/stories become visible in the next deployment (subject to policy)
- dataset releases only become public once they pass promotion gates and validation

---

## Thank you

KFM is only credible if contributors are supported **and** governance is enforced.  
If anything in this guide feels unclear, open a PR to improve it—documentation is a first-class contribution.