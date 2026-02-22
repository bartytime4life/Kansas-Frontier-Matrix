# Contributing to Kansas Frontier Matrix (KFM)

How to contribute **code, data, catalogs, policies, stories, and Focus Mode** changes to KFM while preserving provenance, licensing, sensitivity controls, and reproducibility.

**Status:** Draft  
**Owners:** Maintainers (update `CODEOWNERS` / repo settings)  
🧭 Map-first · ⏱ Time-aware · 🔒 Governed · 🧾 Evidence-first · 📎 Cite-or-abstain

## Quick navigation
- [Non-negotiables](#non-negotiables)
- [Truth path and Promotion Contract](#truth-path-and-promotion-contract)
- [Contribution workflow](#contribution-workflow)
- [Choose the right lane](#choose-the-right-lane)
- [Pull request requirements](#pull-request-requirements)
- [Data and pipeline contributions](#data-and-pipeline-contributions)
- [Catalog, provenance, and evidence contributions](#catalog-provenance-and-evidence-contributions)
- [Documentation and Story Node contributions](#documentation-and-story-node-contributions)
- [Policy contributions](#policy-contributions)
- [Focus Mode contributions](#focus-mode-contributions)
- [Security and sensitive data](#security-and-sensitive-data)
- [Definition of Done](#definition-of-done)
- [Appendix: templates](#appendix-templates)

---

## Non-negotiables

KFM is a **governed system**. If a change bypasses governance, it is treated as a defect—not a feature.

### Trust membrane
- **Clients MUST NOT access storage/DB directly.** All access flows through governed APIs + policy enforcement.
- The UI may **display** policy outcomes and notices; it must **not make** policy decisions.

### Evidence-first + cite-or-abstain
- If you add or modify a factual claim (docs, Story Nodes, Focus Mode behaviors), it must be backed by **EvidenceRefs** that resolve through the evidence resolver.
- If citations cannot be verified for the allowed user context, the correct behavior is **reduce scope or abstain**.

### Policy-as-code (fail-closed)
- Policies are treated as production code: versioned, tested, reviewed, and enforced consistently in CI and runtime.
- CI policy checks must be **merge-blocking**, and runtime policy checks must be **request-blocking**.

### Licensing and rights
- Licenses/rights are operational inputs. If rights are unclear, promotion/publishing is blocked.
- “Metadata-only reference” is acceptable when redistribution is not.

### Sensitive locations and redaction
- Default to **protecting** sensitive locations and private individuals.
- Do not publish precise coordinates unless policy explicitly allows; use generalized derivatives when required.
- Redaction/generalization is a first-class transform and must be recorded in provenance.

### Minimal, reversible increments
- Prefer additive “glue artifacts” (schemas, validators, registries, contracts, ADRs) over intrusive rewrites.
- Every change should be testable, reviewable, and reversible (rollback plan when high risk).

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Truth path and Promotion Contract

Data and governed artifacts move through zones (“truth path”). Promotion is blocked unless the Promotion Contract gates pass.

~~~mermaid
flowchart LR
  RAW[RAW\nappend-only] --> WORK[WORK\nnormalize + QA]
  WORK --> PROCESSED[PROCESSED\npublishable artifacts]
  PROCESSED --> CATALOG[CATALOG/TRIPLET\nDCAT + STAC + PROV]
  CATALOG --> PUBLISHED[PUBLISHED\nAPIs + UI read here]
  RAW --> QUARANTINE[QUARANTINE\nblocked]
  WORK --> QUARANTINE
  QUARANTINE -->|fix issues| WORK
~~~

### Promotion Contract gates (minimum)
You should expect contributions that affect data publication to satisfy:

- **Gate A — Identity & versioning:** deterministic dataset version IDs; immutable once promoted.
- **Gate B — Licensing & rights:** license, rights holder, attribution text, and terms snapshot captured.
- **Gate C — Sensitivity & redaction plan:** policy label assigned; obligations specified and testable.
- **Gate D — Catalog triplet validation:** DCAT/STAC/PROV exist, validate, cross-link; EvidenceRefs resolve.
- **Gate E — Run receipts & checksums:** inputs/outputs digested; environment captured; QA recorded.
- **Gate F — Policy + contract tests:** policy fixtures pass; API/evidence-resolver contract tests pass.
- **Gate G — Operational readiness (recommended):** SBOM/provenance; perf + a11y smoke tests; monitoring.

If a gate fails, the correct posture is **fail-closed**: keep artifacts in WORK/QUARANTINE and fix the gate failure (no “manual promotion”).

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Contribution workflow

### High-level flow
~~~mermaid
flowchart TD
  A[Open Issue or Proposal] --> B[Decide lane + governance impact]
  B --> C[Branch and implement]
  C --> D[Add tests + receipts + catalogs as needed]
  D --> E[Open Pull Request]
  E --> F[CI gates: schemas + policy + contracts]
  F --> G[Review: CODEOWNERS + stewards]
  G --> H[Merge]
  H --> I[Promotion lane: publish governed versions]
~~~

### When to open an Issue first
Open an Issue before a PR if you are proposing any of:
- New dataset onboarding or a new data source
- New policy label/obligation or changes to policy semantics
- New export/download pathway
- Authn/authz changes
- Story publishing rules, evidence resolver changes, or Focus Mode behavior changes
- Any change with likely governance implications (rights, sensitive locations, CARE/consent constraints)

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Choose the right lane

This project may use a repository layout similar to the recommended reference layout. If paths differ, follow the actual repo tree.

| Lane | Typical artifacts | Common gotchas |
|---|---|---|
| Data onboarding | dataset spec, terms snapshot, sensitivity rubric, validation rules | rights ambiguity; missing terms snapshot |
| Pipelines | transforms, container digests, run receipts, QA reports | non-deterministic outputs; missing digests |
| Catalogs | DCAT/STAC/PROV profiles + validators | broken cross-links; incomplete required fields |
| Evidence resolver | EvidenceRef contracts, bundles, policy filtering | leaking restricted metadata; unverifiable citations |
| Stories | Story Node markdown + sidecar map state + citations | missing time window; citations not resolvable |
| Policy | OPA/Rego rules + fixtures + tests | “allow by default”; missing tests |
| UI | map layers config, policy badges/notices, receipt viewer | UI making policy decisions; exposing restricted hints |
| Focus Mode | prompt/versioned configs, evaluation harness, run receipts | citations not verified; prompt injection exposure |

---

## Pull request requirements

### PR basics
- Keep PRs small and focused (one lane / one concern).
- Include a clear “why” and describe governance impact.
- Update docs/contracts/tests in the same PR when behavior changes.

### PR checklist (copy/paste)
- [ ] Scope is minimal and reversible; no unrelated refactors.
- [ ] Tests added/updated (unit/integration/e2e as applicable).
- [ ] Contracts/schemas updated (if any structured data shape changed).
- [ ] Policy changes include fixtures + tests and are reviewed by owners.
- [ ] If data/pipelines changed: run receipts included, digests recorded, QA results attached.
- [ ] If catalogs changed: DCAT/STAC/PROV validate and cross-links resolve.
- [ ] If Story Node changed: sidecar map state updated; all citations resolve.
- [ ] If Focus Mode changed: evaluation harness updated and passing; prompt/version recorded.
- [ ] Rights/licensing implications documented; attribution text included where relevant.
- [ ] Sensitive locations/PII reviewed; outputs generalized/redacted if required.

### Commit hygiene (recommended)
- Use descriptive commit messages (e.g., `policy: default deny for restricted exports`).
- Avoid committing secrets, private keys, tokens, or restricted datasets.

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Data and pipeline contributions

If you add or update a dataset, you typically need all of:
1. **Dataset onboarding spec** (canonical input for deterministic versioning)
2. **Terms snapshot** (license/terms captured at retrieval time)
3. **Sensitivity assessment** + policy label intent + obligations
4. **Transform(s)** with digest-pinned container images
5. **Validation checks** (schema + domain checks)
6. **Run receipt(s)** for the run(s) producing artifacts
7. **Promotion artifacts** (manifests, catalogs, provenance)

### Key rules
- Do not modify promoted artifacts in place; create a new version with new digests.
- Prefer content-addressed artifacts by digest.
- Never embed credentials in dataset specs.

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Catalog, provenance, and evidence contributions

KFM treats catalogs and provenance as **contract surfaces**:
- **DCAT:** dataset identity, publisher, license, distributions
- **STAC:** assets, spatiotemporal extents, file locations
- **PROV:** lineage: inputs, tools, parameters, agents

### Minimum CI expectations (common)
- JSON schema validation for DCAT/STAC/PROV profiles
- Link checking: cross-links exist and resolve
- Evidence resolver contract tests:
  - public evidence resolves to allowed bundles
  - restricted evidence denies without leaking metadata
- spec_hash stability / deterministic output tests

If your change affects evidence resolution, add or update contract tests accordingly.

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Documentation and Story Node contributions

### Docs are production
If a doc changes behavior, governance, or public narrative, treat it as production:
- it must be reviewable,
- testable where possible (lint/linkcheck/schema),
- and policy-labeled when served through governed APIs.

### MetaBlock v2 (no YAML frontmatter)
Use MetaBlock v2 for governed docs, Story Nodes, dataset specs, ADRs, runbooks.

### Story Nodes (v3)
A Story Node is:
- markdown (human narrative)
- sidecar JSON (map state, time window, citations, policy, review state)

Publishing gate: all citations must resolve via the evidence resolver endpoint.

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Policy contributions

### Required posture
- Default deny unless explicitly allowed.
- Keep policies small and composable.
- Add unit tests (golden pass/fail fixtures) to prevent silent drift.
- Version policy packs and reference the active policy version in receipts/manifests.

### Reviews
Policy changes typically require CODEOWNER/steward review because they directly change what can be published or shown.

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Focus Mode contributions

Treat every Focus Mode request like a governed run:
- inputs: user query + optional map view_state + user role/policy context
- outputs: answer text + EvidenceRefs + audit run id

### Hard requirements
- Citations must be verified and policy-filtered before synthesis completes.
- If citations cannot be verified, Focus Mode must abstain or reduce scope.
- Record model identifier, prompt version, retrieval config version, and policy engine version in Focus run receipts.
- Maintain red-team regression scenarios (prompt injection, exfiltration, citation forgery).

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Security and sensitive data

### Threat modeling (minimum)
Before merging changes that affect auth, exports, evidence resolution, or Focus Mode:
- Confirm clients cannot bypass the trust membrane.
- Ensure restricted existence cannot be inferred via error differences.
- Ensure downloads/exports are checked against rights + policy labels.
- Ensure citations are verified and policy-filtered.
- Ensure logs/receipts do not leak restricted data.

### Reporting vulnerabilities
Do not file public issues for security vulnerabilities. Use the project’s private disclosure channel (maintainers will provide contact in repo settings / SECURITY.md if present).

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Definition of Done

A change is “done” when:
- [ ] It is minimal, reversible, and aligns with KFM’s trust membrane + truth path.
- [ ] All relevant CI checks pass (schemas, policy, tests, linkcheck).
- [ ] Governance-sensitive surfaces are reviewed by appropriate owners.
- [ ] Data-related changes include run receipts, digests, and required catalogs/provenance.
- [ ] Story/Focus changes include resolvable citations and policy-safe outputs.
- [ ] Rights/licensing/sensitivity implications are explicit and enforced (not just documented).

[Back to top](#contributing-to-kansas-frontier-matrix-kfm)

---

## Appendix: templates

<details>
<summary>Recommended reference repository layout (adjust to match the real repo)</summary>

~~~text
repo/
  README.md
  docs/
    guides/
    standards/
    adr/
    story/
  data/
    raw/
    work/
    processed/
    catalog/
  policy/
    rego/
    fixtures/
    tests/
  contracts/
    openapi/
    schemas/
    graphql/            (optional)
  src/
    api/
    evidence/
    catalog/
    ingest/
    indexers/
    domain/
  tools/
    validators/
    linkcheck/
    hash/
  tests/
    unit/
    integration/
    e2e/
  .github/
    workflows/
~~~
</details>

<details>
<summary>KFM MetaBlock v2 (no YAML frontmatter)</summary>

~~~text
[KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: <guide|standard|story|dataset_spec|adr|run_receipt>
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<version>
  - kfm://story/<id>@<version>
tags:
  - kfm
notes:
  - <short notes>
[/KFM_META_BLOCK_V2]
~~~
</details>

<details>
<summary>Dataset onboarding spec (canonical input for spec_hash)</summary>

~~~json
{
  "kfm_spec_version": "v1",
  "dataset_slug": "example_dataset",
  "title": "Example Dataset",
  "upstream": {
    "authority": "Example Authority",
    "access_method": "bulk_csv",
    "endpoints": [
      { "name": "primary", "url": "https://example.invalid/data", "parameters": {} }
    ],
    "cadence": "monthly",
    "terms_snapshot": { "license": "TBD", "retrieved_at": "YYYY-MM-DD" }
  },
  "sensitivity": {
    "policy_label_intent": "public",
    "pii_risk": "low|medium|high",
    "sensitive_location_risk": "low|medium|high",
    "obligations": []
  },
  "normalization": { "canonical_fields": {}, "units": {}, "crs": "EPSG:4326" },
  "validation": { "schema": "contracts/schemas/example.schema.json", "checks": [] },
  "outputs": [
    { "artifact_type": "geoparquet", "path": "data/processed/example/<dataset_version_id>/data.parquet" }
  ]
}
~~~
</details>

<details>
<summary>Run receipt (run_record) template</summary>

~~~json
{
  "kfm_run_receipt_version": "v1",
  "run_id": "kfm://run/<timestamp>.<dataset_slug>.<spec_hash_short>",
  "run_type": "pipeline|focus",
  "dataset_slug": "<dataset_slug>",
  "dataset_version_id": "<dataset_version_id>",
  "spec_hash": "sha256:<...>",
  "inputs": [
    { "artifact_id": "kfm://artifact/sha256:<...>", "zone": "raw", "uri": "s3://...", "digest": "sha256:<...>" }
  ],
  "outputs": [
    { "artifact_id": "kfm://artifact/sha256:<...>", "zone": "processed", "path": "data/processed/...", "digest": "sha256:<...>", "media_type": "..." }
  ],
  "validation": { "status": "pass|fail", "reports": [] },
  "policy": { "policy_label": "public|restricted|...", "decision_id": "kfm://policy_decision/<...>", "obligations": [] },
  "environment": { "git_commit": "<commit>", "container_image": "sha256:<image_digest>", "runtime": "kubernetes", "parameters": {} },
  "timestamps": { "started_at": "RFC3339", "ended_at": "RFC3339" }
}
~~~
</details>

<details>
<summary>OPA/Rego policy skeleton (default deny + tests)</summary>

~~~text
# policy/kfm.rego
package kfm.policy

default allow = false

allow {
  input.role == "steward"
}

# Example obligation
obligations["show_notice"] {
  input.policy_label == "public_generalized"
}

# tests/kfm_test.rego
package kfm.policy

test_default_deny {
  not allow with input as {"role": "public"}
}

test_steward_allow {
  allow with input as {"role": "steward"}
}
~~~
</details>
