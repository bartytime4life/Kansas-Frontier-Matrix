# Kansas Frontier Matrix (KFM) — `.github` 🧭🛡️

![Governed Docs](https://img.shields.io/badge/docs-governed-informational)
![Provenance-first](https://img.shields.io/badge/provenance-first-success)
![FAIR%2BCARE](https://img.shields.io/badge/FAIR%2BCARE-aligned-purple)
![Policy-as-Code](https://img.shields.io/badge/policy-as--code-OPA-blue)

> [!IMPORTANT]
> This directory is part of KFM’s “trust membrane”: **contributors and automation should enforce that clients never bypass governed APIs/policies to reach data stores directly**.
> If you change what users can see (data layers, narratives, AI output), expect CI gates to require provenance, policy checks, and validation.

> [!NOTE]
> Some filenames and workflows below are **recommended defaults** and may differ in your repository. If a path is missing, treat it as **(not confirmed in repo)** and align it to the canonical standards in `docs/`.

---

## Table of contents

- [Why `.github` exists](#why-github-exists)
- [Directory layout](#directory-layout)
- [CI quality gates](#ci-quality-gates)
- [CI flow](#ci-flow)
- [Local preflight](#local-preflight)
- [Pull request checklist](#pull-request-checklist)
- [Governance and sensitive information](#governance-and-sensitive-information)
- [Key internal references](#key-internal-references)

---

## Why `.github` exists

KFM is an evidence-first, provenance-centric geospatial system (pipelines + catalogs + knowledge graph + governed API + map/timeline UI + Story Nodes + Focus Mode). This directory operationalizes that stance in GitHub by housing:

- **CI workflows** (lint/validate/test/build gates)
- **Contribution UX** (issue forms, PR template, CODEOWNERS)
- **Security / policy entry points** (as applicable)

The goal: keep changes reviewable and safe-by-design—especially for provenance, governance, and sensitive-location handling.

---

## Directory layout

> [!TIP]
> If you add new automation, prefer small, composable workflows with clear names and explicit “what/why” descriptions.

```text
.github/
  README.md                        # (this file) how GitHub automation enforces KFM gates
  workflows/
    docs.yml                       # docs lint + structure + link + accessibility + sensitivity
    data-catalog.yml               # STAC/DCAT/PROV validation + provenance checks
    api-contracts.yml              # OpenAPI/GraphQL contract & compatibility checks
    policy.yml                     # OPA/Rego unit tests (+ “fail closed” posture checks)
    e2e.yml                        # UI + API end-to-end tests (provenance panel, citations)
    supply-chain.yml               # SBOM + provenance attestations (SLSA/in-toto)
  ISSUE_TEMPLATE/
    bug_report.yml
    feature_request.yml
    story_node.yml                 # optional: Story Node proposal intake
  PULL_REQUEST_TEMPLATE.md
  CODEOWNERS
  dependabot.yml                   # optional
  SECURITY.md                      # optional
```

---

## CI quality gates

> [!WARNING]
> CI gates are not “nice to have” in KFM. Docs, data, and policy are governed artifacts: **a PR that weakens validation or provenance requirements should be treated as a governance change**.

### Gate registry

| Gate | What it checks | Why it exists | Typical implementation notes |
|---|---|---|---|
| Docs lint + structure | Markdown lint, heading order, template compliance | Prevents drift from governed templates; keeps docs machine-ingestible | Often paired with link-check + accessibility |
| Provenance rules | “No claim without evidence,” references resolved | Supports “cite-or-abstain” behavior and auditability | Treat missing evidence as **blockers** |
| Link integrity | No broken internal links/images | Keeps docs renderable & CI-clean | Include relative-link checks |
| Accessibility | Alt text, table headers, heading hierarchy | Makes docs usable and reviewable | Fail on missing alt text for meaningful images |
| Sensitivity scanning | Flags sensitive content (e.g., precise locations) | Prevents unsafe exposure; protects culturally sensitive data | Prefer redaction/generalization; add review flags |
| Data catalog validation | STAC / DCAT v3 / PROV(-O) structure | Ensures interoperability and traceable lineage | Validate JSON + JSON-LD where applicable |
| API contract checks | OpenAPI diffs; consumer contract tests | Prevents breaking clients; keeps API governed | Require versioning + compatibility notes |
| Policy-as-code tests | OPA/Rego unit tests for allow/deny | Ensures governance gates behave predictably | Default-deny / fail-closed posture |
| End-to-end flows | UI provenance panel; Story Node citations; Focus Mode citation resolution | Ensures provenance UX works in practice | Treat “citation missing” as failure |
| Supply chain integrity | SBOM + provenance attestations | Hardens build integrity | Generate SPDX + SLSA/in-toto attestations |

> [!NOTE]
> If your repo uses different names (or split workflows), keep the gate semantics stable and update this README accordingly.

---

## CI flow

```mermaid
flowchart LR
  PR[Pull Request] --> Lint[Docs lint + structure checks]
  PR --> Schema[Data schema validation\n(STAC/DCAT/PROV)]
  PR --> Contracts[API contract checks\n(OpenAPI/GraphQL)]
  PR --> Policy[OPA policy tests\n(default deny / fail closed)]
  PR --> E2E[End-to-end flows\n(UI provenance + citations)]
  PR --> Supply[SBOM + provenance attestations]

  Lint --> Merge{Merge allowed?}
  Schema --> Merge
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

If you are modifying pipelines, policies, or contracts, also run the relevant local test commands for those subsystems **(not confirmed in repo)**.

---

## Pull request checklist

- [ ] **Scope is declared** (docs / data / backend / web / policy)
- [ ] **Provenance included** for every substantive claim or new layer/story assertion
- [ ] **Sensitive content reviewed**: precise locations redacted/generalized; review flags added
- [ ] **Docs are template-aligned** (if using governed templates)
- [ ] **Policy impact assessed** (OPA rules updated + tests added where needed)
- [ ] **Contracts updated** (OpenAPI/GraphQL) with compatibility notes
- [ ] **Validators and tests pass** locally (or explain why CI should be the source of truth)
- [ ] **No trust-membrane violations** (no direct DB access from UI/external clients)

---

## Governance and sensitive information

KFM is committed to:

- **FAIR** (Findable, Accessible, Interoperable, Reusable)
- **CARE** (Collective Benefit, Authority to Control, Responsibility, Ethics)

Practical implications for GitHub work:

- Treat docs/data/policies as **governed artifacts**, not “just text.”
- Avoid publishing **precise locations** of sacred/vulnerable sites.
- If content touches Indigenous histories or culturally restricted information, add an explicit **review trigger** in the PR description and route to governance reviewers **(process specifics may vary by repo)**.

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

</details>