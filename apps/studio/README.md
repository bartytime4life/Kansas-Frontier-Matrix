# KFM Studio
Governed authoring + review UI for **Story Nodes (v3)** — evidence-first narratives that can only be published when **citations resolve**.

**Status:** 🚧 Scaffold / wiring-in-progress  
**Owners:** _TBD_ (add CODEOWNERS entry for `apps/studio/`)  
**Scope:** Story authoring & review workflow (draft → validate → review → publish)

![status](https://img.shields.io/badge/status-scaffold-lightgrey)
![governance](https://img.shields.io/badge/governance-fail--closed-blue)
![citations](https://img.shields.io/badge/citations-must%20resolve-critical)
![a11y](https://img.shields.io/badge/accessibility-required-informational)

**Jump to:** [Overview](#overview) • [Non-negotiables](#non-negotiables) • [Workflows](#workflows) • [Architecture](#architecture) • [Local development](#local-development) • [Testing and CI gates](#testing-and-ci-gates) • [Governance and safety](#governance-and-safety) • [Contributing](#contributing)

---

## Overview

KFM Studio is the place where contributors create and revise **Story Nodes** — narrative artifacts intended to be published under KFM’s governance rules.

Studio exists to make “governance-by-construction” practical in daily authoring:

- Write stories as **structured, reviewable artifacts**
- Attach **evidence** to every claim
- Run the same **validation gates** locally that CI will enforce
- Move content through a **review workflow**
- **Fail closed** at publish time if citations/evidence cannot be resolved

> If you’re looking for map browsing / layer toggles / feature inspection, that’s **Map Explorer** (separate UI). Studio is for _making_ and _reviewing_ Story content.

---

## Non-negotiables

These are system invariants Studio must enforce (or make impossible to bypass):

1. **Publish is gated:** a Story Node can’t be published unless its citations/evidence resolve.
2. **Trust membrane:** Studio is a client — it must never talk directly to databases or storage. All reads/writes go through governed interfaces (API + policy boundary).
3. **Policy-aware rendering:** if the user lacks access (or the content is restricted), Studio must show safe alternatives (redaction/generalization/abstention UX) rather than “best-effort” leakage.
4. **Auditability:** editing, review decisions, and publish actions must be attributable and reconstructable (who/what/when/why).

---

## Workflows

### Draft → validate → review → publish

```mermaid
flowchart LR
  A[Draft in Studio] --> B[Validate locally<br/>schema + links + evidence refs]
  B --> C[Submit for review]
  C -->|Changes requested| A
  C --> D[Citations/evidence resolve gate]
  D -->|Pass| E[Publish]
  D -->|Fail closed| A
```

### Roles and expectations

> This table is a **default** starting point. Adjust once the repo has a formal roles/RACI document.

| Role | Draft | Request review | Approve | Publish |
|---|---:|---:|---:|---:|
| Contributor | ✅ | ✅ | ❌ | ❌ |
| Steward / Reviewer | ✅ (edits) | ✅ | ✅ | ✅/❌ (policy-dependent) |
| Operator | ❌ | ❌ | ❌ | ✅ (release/promotion mechanics) |
| Council | ❌ | ❌ | ✅ (high-sensitivity decisions) | ✅ (exception pathways) |

---

## Story Node contracts

Studio should treat Story Nodes as **schema-backed** content with required metadata and explicit evidence references.

### KFM MetaBlock v2

At minimum, Studio should be able to **create/edit/validate** these metadata fields (exact on-disk format is repo-defined):

- `story_id`
- `title`, `summary`
- `authors`
- `created_at`, `updated_at`
- `time_coverage`, `geography_coverage`
- `dataset_refs`, `evidence_refs`
- `policy_label`
- `review_status`
- `revision_history`

### Evidence model expectations

Studio UX should make it hard to “hand-wave” evidence:

- Every claim (or claim group) must link to at least one **EvidenceRef**
- Studio should offer “resolve now” and show the resolved **EvidenceBundle** (when accessible)
- Broken links / missing evidence should be treated as **blocking errors** for publish

---

## Architecture

### Boundary diagram

```mermaid
flowchart TB
  subgraph Client
    S[Studio (web app)]
  end

  subgraph GovernedSurface
    API[Governed API<br/>contract-first boundary]
    POL[Policy engine<br/>default-deny]
    EVD[Evidence resolver<br/>EvidenceRef → EvidenceBundle]
  end

  subgraph DataPlane
    CAT[Catalogs<br/>DCAT / STAC / PROV]
    IDX[Search index<br/>projections]
    AUD[Audit ledger / receipts]
  end

  S --> API
  API --> POL
  API --> EVD
  EVD --> CAT
  API --> IDX
  API --> AUD
```

### What Studio should never do

- Direct S3/object-store reads of restricted content
- Direct DB queries (Neo4j, Postgres, etc.)
- “Helpful” fallbacks that display restricted details when a resolver/policy says “deny”
- Publishing that bypasses validation and citation resolution

---

## Local development

> Tooling, scripts, and package manager are **not assumed** here. Use this section as a checklist and update it once `apps/studio/package.json` (and lockfile choice) are confirmed.

### Prerequisites

- Node.js runtime (version pinned by repo conventions — **TBD**)
- Repo-standard package manager (**TBD**: npm / pnpm / yarn)
- A running **Governed API** (or a mocked API mode for local dev)

### Typical workflow

1. Install dependencies (repo root)
2. Configure Studio to point at the Governed API
3. Start dev server
4. Run validation + tests before opening a PR

### Environment configuration

Prefer an `apps/studio/.env.example` checked into the repo (if missing, add one). Common values Studio tends to need:

- `KFM_API_BASE_URL` — base URL for the governed API gateway
- `KFM_AUTH_*` — OIDC issuer/client settings (if auth is in place)
- `KFM_PUBLIC_BASE_URL` — used for preview links (if applicable)

---

## Testing and CI gates

Studio changes should expect merge-blocking gates aligned with KFM governance:

- ✅ lint + typecheck
- ✅ Story Node template/schema validation
- ✅ policy tests (where Studio touches policy-aware UI)
- ✅ link checking (no broken citations/evidence)
- ✅ security scanning (dependencies)
- ✅ accessibility smoke checks (keyboard navigation + core flows)

### What to test (minimum)

- Draft save/restore (including MetaBlock fields)
- Evidence linking UX (add/remove/resolve EvidenceRefs)
- “Citations won’t resolve” failure path is clear and blocks publish
- Restricted content handling (deny/generalize/abstain UI is correct)
- Review transitions (draft → in review → approved/published) are auditable

---

## Governance and safety

### Sensitive locations and restricted material

Studio must assume some locations and datasets are sensitive. UI patterns should:

- Avoid displaying exact coordinates for restricted/sensitive items
- Prefer generalized geometry, aggregation, or “withheld” summaries
- Require explicit governance review for exceptions

### Trust surfaces

Studio should make trust legible:

- Show “why I can/can’t show this” for restricted items
- Show license + provenance pointers where available
- Surface validation failures as actionable items (not hidden logs)

---

## Contributing

- Keep changes PR-sized and reversible.
- Prefer additive “glue artifacts” (schemas, validators, contract tests, UI components) over intrusive rewrites.
- Don’t introduce new publish paths without updating **policy gates** and **tests**.

### Definition of Done (Studio PR)

- [ ] UI respects policy boundaries (no bypass paths)
- [ ] Story Nodes validate locally and in CI
- [ ] Citation resolution gate is enforced for publish
- [ ] Accessibility smoke checks pass for authoring + review flows
- [ ] Tests cover at least one “deny/generalize” restricted scenario
- [ ] Any new metadata fields are documented and schema-backed

---

## Troubleshooting

### “Publish is blocked: citations won’t resolve”
- Confirm the EvidenceRefs are valid and reachable
- Confirm the Governed API evidence resolver is running and reachable
- Confirm your access level/policy_label permits resolution

### “I can view the story but can’t see sources”
- Likely a policy denial or resolver error; Studio should show the denial reason code and next step

### “A11y gate failed”
- Verify keyboard navigation for the authoring form and evidence panels
- Ensure focus order is logical; check ARIA labeling on controls

---

## Appendix: Glossary

- **Story Node (v3):** Governed narrative artifact with metadata, claims, and evidence references.
- **EvidenceRef:** Pointer to an authoritative source (dataset version, document, archive item).
- **EvidenceBundle:** Resolver output that packages evidence + provenance + license + policy context.
- **policy_label:** Classification used to decide what can be shown and to whom.
- **Fail closed:** If validation/policy/evidence checks fail, nothing publishes.
