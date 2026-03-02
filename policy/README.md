<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8f4c5db9-1cc2-4a2f-b5b3-fb8c6a9a8e7d
title: policy/README.md
type: standard
version: v1.2
status: draft
owners: KFM Governance + Policy Stewards (TODO: set via CODEOWNERS)
created: 2026-02-26
updated: 2026-03-02
policy_label: public
related:
  - kfm://doc/KFM-GDG-2026                 # TODO: link to in-repo copy of the Governance Guide
  - kfm://doc/KFM-AGDP-2026-02-27          # TODO: Architecture, Governance, and Delivery Plan (2026-02-27)
  - kfm://doc/KFM-DDGG-vNext-2026-02-20    # TODO: Definitive Design & Governance Guide (vNext)
tags: [kfm, policy, governance, opa, rego, ci, promotion-contract, evidence-resolver, rights, sensitivity, audit, bundle]
notes:
  - Directory README for the policy bundle (CI + runtime semantics).
  - Replace <ORG>/<REPO> badge placeholders once repo metadata is known.
  - This README is written to be executable: every rule category must have fixtures + tests.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `policy/` — Governed, fail-closed policy-as-code for KFM (OPA/Rego)

**Purpose:** This directory contains the **policy bundle** (OPA/Rego or equivalent) that enforces KFM governance:
**access control**, **licensing/rights**, **sensitivity/redaction**, **promotion gates**, and **policy-safe error shaping** — with **the same semantics in CI and at runtime**.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Posture](https://img.shields.io/badge/posture-default--deny-critical)
![OPA Bundle](https://img.shields.io/badge/opa-bundle-blue)
![Rego](https://img.shields.io/badge/rego-v1%20ready-blueviolet)
![CI/Runtime](https://img.shields.io/badge/ci%2Fruntime-semantics%20match-important)
![Fixtures](https://img.shields.io/badge/fixtures-required-informational)
![Tests](https://img.shields.io/badge/tests-required-informational)
![Audit](https://img.shields.io/badge/audit-reconstructable-success)

<!-- TODO(repo): Replace <ORG>/<REPO> and workflow filenames -->
<!-- ![Policy Tests](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/policy-tests.yml?branch=main) -->
<!-- ![Conftest Gate](https://img.shields.io/github/actions/workflow/status/<ORG>/<REPO>/conftest.yml?branch=main) -->

> **TL;DR:** In KFM, **security is governance**. Policy is the shared source of truth for what is allowed to be served, exported, or claimed — and it must be **deterministic**, **fixture-backed**, **test-covered**, and **fail-closed**.

> [!NOTE]
> **Normative keywords used here**
> - **MUST** = required for compliance with the trust membrane / promotion contract.
> - **SHOULD** = strongly recommended to preserve auditability and prevent drift.
> - **MAY** = optional; adopt when useful.

---

## Quick navigation

- [Where this fits in KFM](#where-this-fits-in-kfm)
- [What lives here](#what-lives-here)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Policy pack contract](#policy-pack-contract)
- [Policy decision envelope](#policy-decision-envelope)
- [Truth path and promotion gates](#truth-path-and-promotion-gates)
- [Evidence resolver and citations](#evidence-resolver-and-citations)
- [Sensitivity and rights defaults](#sensitivity-and-rights-defaults)
- [Policy labels and controlled vocab](#policy-labels-and-controlled-vocab)
- [CI gates and local commands](#ci-gates-and-local-commands)
- [Making changes](#making-changes)
- [Directory layout](#directory-layout)
- [FAQ](#faq)

---

## Where this fits in KFM

This directory is part of the **trust membrane**. It defines the rules used by:

- **CI gates** (PR merge blockers)
- **Runtime Policy Enforcement Points (PEPs)**:
  - Governed API (data serving, exports, tiles)
  - Evidence resolver (EvidenceRef → EvidenceBundle)
  - Pipeline runner + promotion system (promotion gates)

> [!IMPORTANT]
> **UI is not a policy engine.** UI renders policy outcomes (badges/notices), but authorization/redaction/export decisions MUST happen behind the trust membrane.

```mermaid
flowchart LR
  subgraph CI["CI and PR gates"]
    PR["Pull Request"] --> Gate["OPA or Conftest policy gate"]
    Gate --> Merge["Merge allowed only if gates pass"]
  end

  subgraph Runtime["Runtime enforcement"]
    API["Governed API PEP"] --> PDP["Policy Decision Point"]
    ER["Evidence Resolver PEP"] --> PDP
    Pipe["Pipeline and Promotion PEP"] --> PDP
  end

  UI["Map, Story, Focus UI"] --> API
  UI --> ER
```

[Back to top](#top)

---

## What lives here

### ✅ Acceptable inputs

What belongs in `policy/`:

- **Policy code** (Rego packages or equivalent) for:
  - authorization (role/label/action rules)
  - rights/licensing enforcement *(“online availability” ≠ permission to reuse)*
  - sensitivity + redaction/generalization obligations
  - promotion gating decisions (fail closed)
  - policy-safe error shaping (no restricted inference)
- **Fixtures** that represent policy decisions:
  - allow/deny outcomes
  - obligations arrays
  - stable reason codes for auditability
- **Policy tests**:
  - OPA unit tests (`opa test`)
  - and/or Conftest tests used as PR gates
- **Rubrics** used as policy inputs:
  - licensing classification rubric
  - sensitivity rubric + generalization guidance
- **Controlled vocabularies** referenced by policy:
  - `policy_label` list
  - obligation types and reason codes (recommended)

### 🚫 Exclusions

What must **not** go in `policy/`:

- **Secrets** (API keys, credentials, private tokens).
- **Raw datasets** or restricted artifacts (policy should reference **metadata**, not embed sensitive content).
- **UI logic** (UI may display policy outcomes but must not decide policy).
- **One-off exceptions** without fixtures + tests (exceptions must become governed, testable policy).

> [!WARNING]
> If a rule cannot be tested (fixtures + tests), it is not policy — it’s a suggestion. Policy MUST be deterministic and CI-enforced.

[Back to top](#top)

---

## Non-negotiable invariants

These invariants align to KFM north stars. Policy MUST **enforce** them, not merely describe them.

### 1) Default deny

- Unknown = **deny**.
- Missing metadata = **deny** (or quarantine).
- Unhandled `policy_label` = **deny**.
- Unrecognized action/resource type = **deny**.

### 2) Trust membrane

- Clients/UI MUST NOT gain access to storage/DB/indexes by policy loophole.
- Policy MUST assume access happens only through governed surfaces (API, evidence resolver, pipeline runner).
- “Allowed” MUST NOT imply “bypass”: obligations still apply.

### 3) Evidence-first

- Any “allowed to claim/serve” decision MUST be compatible with evidence-first UX:
  - evidence must be resolvable (or UI must degrade/abstain)
  - license/rights must be present where required
  - provenance/receipts must be linkable where policy allows

### 4) Cite-or-abstain

- If citations cannot be verified and policy-allowed, Focus Mode MUST **abstain** or reduce scope.
- Policy SHOULD return stable reason codes + safe alternatives to support abstention UX.

### 5) Promotion Contract support

- Policy participates in promotion gates and MUST be able to deny promotion for:
  - missing license/rights
  - missing/unclear sensitivity handling
  - missing receipts/checksums policy fields
  - missing catalogs required for the dataset class (when applicable)

### 6) Canonical vs rebuildable

- Policy MUST treat projections/caches as rebuildable and never as authoritative truth.
- If a projection contradicts canonical catalogs/receipts, policy SHOULD bias toward **deny** or **degrade** until resolved.

### 7) Deterministic identity and hashing

- Policy MUST NOT depend on unstable, non-deterministic fields as decision inputs.
- Identity/versioning rules SHOULD operate on stable identifiers (`dataset_version_id`, `spec_hash`) and be fixture-tested.

### 8) Policy-safe errors

- A public caller MUST NOT infer restricted resources through:
  - 403 vs 404 differences
  - different error messages
  - different payload shapes
  - “helpful” metadata in errors
- Policy SHOULD support an indistinguishable, safe error posture for restricted objects.

[Back to top](#top)

---

## Policy pack contract

KFM treats policy as a **packaged contract**, not loose `.rego` files. The pack MUST be:

- **Buildable** into an OPA bundle (or equivalent)
- **Versioned** (pack version or digest)
- **Pinned** for audits (receipts record what pack evaluated a decision)
- **Compatible** between CI and runtime (same fixtures → same outcomes)

### Pack identity (recommended)

Policy SHOULD expose (as data or metadata) a `policy_pack_id`, e.g.:

- a bundle `revision` (often a git SHA)
- a content digest (sha256)
- or an artifact digest if distributed via OCI/registry

> [!NOTE]
> Exact identity mechanism depends on your repo/release tooling; do not claim a specific mechanism exists until repo release process is verified.

### Bundle manifest requirements (OPA bundles)

If using OPA bundles, the `.manifest` file is part of the contract:

- `revision`: identifies the bundle revision
- `rego_version`: global Rego syntax version (0 or 1)
- `file_rego_versions`: per-file overrides (if mixing v0/v1 during migration)
- `roots`: scopes what the bundle owns (defaults to everything if omitted)
- signing metadata if using signed bundles

**Illustrative `.manifest`** (v1 syntax, scoped roots):

```json
{
  "revision": "git:abcdef123456",
  "rego_version": 1,
  "roots": ["kfm"]
}
```

> [!WARNING]
> If `roots` is omitted, OPA treats the bundle as owning **all** policy/data roots. Only omit `roots` intentionally.

[Back to top](#top)

---

## Policy decision envelope

Policy evaluation MUST return a **decision envelope** that is stable, auditable, and easy to test.

### Required decision fields

- `decision`: `allow | deny` *(default deny)*
- `policy_label`: controlled vocabulary string for the resource
- `obligations[]`: required follow-up actions (redaction, notices, export constraints)
- `reason_codes[]`: stable identifiers for audit + debugging without leaking sensitive info

### Strongly recommended fields

- `decision_id`: stable identifier for correlation in receipts/PROV
- `policy_pack_id`: bundle digest or version identifier used for evaluation
- `audit_ref`: correlation ID for policy-safe error responses and steward debugging

> [!NOTE]
> **Receipts and manifests SHOULD reference policy decisions.** Treat missing policy references as **non-auditable** and deny/quarantine.

### Obligations

Obligations make “allowed” safe, and MUST be enforceable by downstream systems:

- `show_notice`: UI must show a banner (e.g., “generalized due to policy”).
- `redact_fields`: evidence resolver must redact before returning.
- `force_generalization`: serve a `public_generalized` derivative only.
- `suppress_export`: block downloads/exports for the caller/action.
- `require_attribution`: exports must include license + attribution text.
- `log_audit`: require audit emission for this action.

### Policy-safe error shaping

Policy SHOULD support a safe error model that avoids restricted inference.

- **Public caller:** return a generic “not found or not permitted” response for restricted targets.
- **Authorized steward/operator:** return explicit deny with reason codes and remediation hints.

> [!WARNING]
> Do not include restricted labels, precise coordinates, or rights-holder details in public error responses.

[Back to top](#top)

---

## Truth path and promotion gates

KFM’s lifecycle is an auditable truth path with storage zones + validation gates. Policy participates in gates, and promotion to governed runtime surfaces is blocked unless minimum gates are met.

```mermaid
flowchart LR
  RAW["RAW"] --> WORK["WORK or Quarantine"] --> PROCESSED["PROCESSED"] --> CATALOG["CATALOG triplet"] --> PUBLISHED["PUBLISHED"]
  Gate["Policy plus Promotion Contract gates"] -.enforce.-> WORK
  Gate -.enforce.-> PROCESSED
  Gate -.enforce.-> CATALOG
  Gate -.enforce.-> PUBLISHED
```

> [!IMPORTANT]
> “Publish” is not a UI action; it is a governed promotion event. If the system cannot answer
> **“Is it safe and permitted to publish?”** deterministically, the correct result is **deny/quarantine**.

### Gate map (policy participation examples)

| Gate | Promotion gate | Policy participation examples |
|---:|---|---|
| A | Identity & versioning | deny if required IDs/spec-hash inputs missing or invalid |
| B | Licensing & rights metadata | deny if license/rights/attribution missing or incompatible with intended distribution |
| C | Sensitivity classification & redaction plan | deny if restricted/sensitive lacks recorded generalization/redaction plan |
| D | Catalog triplet validation | deny if required catalog links missing; deny if EvidenceRefs cannot resolve |
| E | QA & thresholds | deny (or quarantine) if QA report missing or thresholds failed |
| F | Run receipt & audit record | deny if receipts omit required decision fields or omit policy references |
| G | Release manifest | deny if promotion not recorded as a manifest referencing artifact digests |

[Back to top](#top)

---

## Evidence resolver and citations

In KFM, a “citation” is not a pasted URL. It is an **EvidenceRef** that resolves — via the evidence resolver — into an **EvidenceBundle** containing metadata, artifacts, and provenance needed to inspect and reproduce the claim.

**Hard gate behavior**
- Focus Mode and Story publishing MUST require: every citation resolves and is policy-allowed.
- If not, the system MUST narrow scope or abstain.

> [!TIP]
> Treat citation verification as the primary anti-hallucination mechanism for narrative surfaces.

[Back to top](#top)

---

## Sensitivity and rights defaults

These defaults are aligned to KFM posture and should be encoded as policy rules + fixtures.

### Sensitivity defaults

- Default deny for **restricted** and **restricted_sensitive_location**.
- If any public representation is allowed, produce a separate `public_generalized` dataset version.
- Never leak restricted metadata through error behavior.
- Do not embed precise coordinates in Story Nodes or Focus Mode outputs unless policy explicitly allows.
- Treat redaction/generalization as a first-class transform recorded in PROV.

### Licensing and rights enforcement

- Principle: **online availability does not equal permission to reuse**.
- Promotion gate SHOULD require license + rights metadata for every distribution.
- “Metadata-only reference” mode SHOULD be allowed: catalog without mirroring if rights do not allow.
- Export functions SHOULD include attribution and license text automatically.
- Story publishing gate SHOULD block if rights are unclear for included media.

> [!IMPORTANT]
> Licensing is not paperwork. It is a policy input.

[Back to top](#top)

---

## Policy labels and controlled vocab

Policy labels are controlled vocabulary values attached to datasets, stories, and evidence bundles.

### `policy_label` table (starter set)

| `policy_label` | Meaning | Default posture | Typical obligations |
|---|---|---|---|
| `public` | Safe for public display/download | allow for public `read` | require_attribution |
| `public_generalized` | Public-safe derived representation | allow for public `read` | show_notice; provenance link to generalization |
| `internal` | Visible to authenticated org users | deny to public | log_audit |
| `restricted` | Access limited to stewards/authorized roles | deny by default | policy_safe_error; log_audit |
| `restricted_sensitive_location` | Restricted + location-sensitive | deny by default | force_generalization; redact_fields; policy_safe_error |
| `embargoed` | Hidden until date/review | deny by default | embargo_until; log_audit |
| `quarantine` | Not promotable/servable | deny always | remediation_hint |

> [!IMPORTANT]
> Adding a new `policy_label` is a governance change:
> update vocabulary → update fixtures → update tests → update dependent validators/exports.

### Controlled vocab rules

- Vocabularies MUST be versioned (e.g., `policy_labels.v1.yml`).
- Policy MUST fail closed on unknown vocab values.
- CI SHOULD run a vocab linter that blocks merges on drift.

[Back to top](#top)

---

## CI gates and local commands

KFM requires CI to encode governance invariants as **merge-blocking tests**.

### CI gate matrix (recommended)

| Gate | Tooling | Must block merge | Notes |
|---|---|---:|---|
| Rego format | `opa fmt` | ✅ | Deterministic formatting reduces drift and review noise |
| Rego static checks | `opa check` | ✅ | Use strict checks to catch invalid/unsafe patterns early |
| Policy unit tests | `opa test` | ✅ | Coverage for allow/deny + obligations + error shaping |
| Fixture evaluation | `conftest test` | ✅ | Runs policy against fixture inputs; produces readable deny output |
| Vocabulary validation | JSON/YAML schema + policy | ✅ | Unknown policy_label/obligation/reason_code must fail closed |

### Recommended local commands

```bash
# 1) Format
opa fmt -w policy/rego

# 2) Static checks (strict)
opa check --strict policy/rego

# 3) Unit tests
opa test -v policy/rego policy/tests

# 4) Fixture-driven PR gate style checks (if using conftest)
conftest test -p policy/rego policy/fixtures
```

> [!IMPORTANT]
> **Rego v1 migration note:** Some tooling (notably Conftest) has changed defaults over time.
> Pin tool versions in CI and be explicit about Rego version where needed.

[Back to top](#top)

---

## Making changes

Policy changes are governance changes. Treat them with the same discipline as schema/API changes.

### Change rules

- **No silent changes:** every change MUST add/modify fixtures and tests.
- **Fail closed:** unhandled labels/actions default to deny.
- **CI/runtime parity:** outcomes MUST match between CI evaluation and runtime PDP evaluation.
- **Policy-safe outputs:** no restricted inference through error models or payload differences.

### PR checklist

- [ ] Rego change includes stable `reason_codes` (or documented rationale).
- [ ] Fixtures cover decision **and obligations** (not just allow/deny).
- [ ] Tests cover at least:
  - public role (deny-by-default posture)
  - steward role (explicit allows where intended)
  - restricted existence inference protections
  - export/download constraints (rights + obligations)
- [ ] If vocab changed: update vocab files + downstream fixtures/tests.
- [ ] Steward review requested and recorded (via CODEOWNERS / reviewers).

> [!TIP]
> Prefer adding new rules behind fixtures, then expanding coverage, before widening allow conditions.

[Back to top](#top)

---

## Directory layout

This is a **recommended adoption target**. Adjust if your repo differs, but preserve:
**rego + fixtures + tests + vocab + rubrics**.

> [!NOTE]
> Do not claim specific modules or paths exist until verified in the live repo. Treat this layout as an adoption target and evolve it in small, reversible steps.

```text
policy/
├─ README.md
├─ conftest.toml                                 # Optional: conftest config (namespaces, output, ignore rules)
│
├─ registry/                                     # Machine-readable registry + schemas + fixtures (small)
│  ├─ policy_bundle.v1.json                      # Policy bundle manifest (packages, versions, entrypoints, required tests)
│  ├─ schemas/                                   # Schemas for registries + decision/fixture shapes (optional, recommended)
│  │  ├─ policy_bundle.v1.schema.json
│  │  ├─ decision_envelope.v1.schema.json        # {decision, policy_label, obligations[], reason_codes[], policy_pack_id?}
│  │  ├─ fixture_input.v1.schema.json            # {user, action, resource, context}
│  │  ├─ obligation.v1.schema.json               # obligation object shape(s)
│  │  ├─ reason_codes.v1.schema.json             # reason code enumerations / structure
│  │  └─ vocab_list.v1.schema.json               # schema for YAML vocab lists (if validated)
│  └─ fixtures/
│     ├─ valid/
│     │  ├─ policy_bundle.minimal.json
│     │  └─ decision_envelope.minimal.json
│     └─ invalid/
│        ├─ decision_envelope.missing_reason_codes.json
│        └─ fixture_input.missing_policy_label.json
│
├─ rego/                                         # Policy packages (OPA/Rego)
│  ├─ kfm/                                       # Namespace root (recommended)
│  │  ├─ decision.rego                           # Canonical decision envelope builder (default deny)
│  │  ├─ authz.rego                              # allow/deny rules (role/action/resource)
│  │  ├─ labels.rego                             # label semantics helpers (public vs restricted, etc.)
│  │  ├─ obligations.rego                        # obligation derivation (show_notice, redact_fields, suppress_export…)
│  │  ├─ rights.rego                             # license/rights enforcement rules (export, attribution, redistribution)
│  │  ├─ sensitivity.rego                        # sensitive-location + PII posture + generalization requirements
│  │  ├─ promotion.rego                          # promotion gate participation (deny if missing required artifacts)
│  │  ├─ evidence.rego                           # EvidenceRef/EvidenceBundle rules (resolvability requirements, obligations)
│  │  ├─ exports.rego                            # download/export policy (policy_label + rights + obligations)
│  │  ├─ focus.rego                              # cite-or-abstain rules (citation verification hard gate outcomes)
│  │  ├─ audit.rego                              # audit/logging obligations + required fields (audit_ref, run_id, reason_codes)
│  │  └─ errors.rego                             # policy-safe error shaping (no restricted inference)
│  │
│  └─ _shared/                                   # Common helpers (pure functions; no policy decisions)
│     ├─ canonical_json.rego                     # deterministic JSON helpers (avoid hash drift)
│     └─ geo.rego                                # bbox/geometry guards (no precise leakage)
│
├─ fixtures/                                     # Deterministic decision fixtures (synthetic; safe-by-default)
│  ├─ README.md
│  ├─ inputs/
│  └─ expected/
│
├─ tests/                                        # Rego unit tests (or conftest rules)
│  ├─ README.md
│  ├─ authz_test.rego
│  ├─ rights_test.rego
│  ├─ sensitivity_test.rego
│  ├─ promotion_test.rego
│  ├─ evidence_test.rego
│  └─ policy_safe_errors_test.rego
│
├─ vocab/                                        # Controlled vocabulary lists (versioned; referenced by policy + CI)
│  ├─ README.md
│  ├─ policy_labels.v1.yml
│  ├─ obligations.v1.yml
│  ├─ reason_codes.v1.yml
│  ├─ roles.v1.yml
│  ├─ actions.v1.yml
│  └─ resource_types.v1.yml
│
└─ rubrics/                                      # Human-readable + machine-referenced policy inputs
   ├─ README.md
   ├─ licensing.md
   ├─ sensitivity.md
   └─ generalization_guidance.md
```

[Back to top](#top)

---

## FAQ

### Why default deny?

Because “unknown” is not the same as “allowed.” Default deny prevents accidental leakage and forces explicit governance decisions.

### Why obligations?

Some “allowed” results are only safe when accompanied by safeguards (notices, generalization, redaction, export controls). Obligations make those safeguards enforceable.

### Can the UI decide policy?

No. UI can only render policy outcomes and trust badges/notices. Authorization, redaction, and export decisions happen behind the trust membrane.

### What happens when evidence can’t be verified?

For Focus Mode and other citation-bearing surfaces: **abstain or reduce scope**. Do not guess; do not fabricate citations; do not bypass the evidence resolver.

[Back to top](#top)

---

## Appendix

<details>
<summary><strong>Suggested policy input shape (illustrative)</strong></summary>

```json
{
  "user": { "principal": "user:alice", "role": "public", "groups": [] },
  "action": "read",
  "resource": {
    "type": "dataset",
    "dataset_version_id": "2026-02.abcd1234",
    "policy_label": "public"
  },
  "context": {
    "purpose": "browse",
    "view_state": {
      "bbox": [-102.0, 36.9, -94.6, 40.0],
      "time_window": { "start": "1950-01-01", "end": "2024-12-31" }
    }
  }
}
```
</details>

<details>
<summary><strong>Minimal Rego skeleton (illustrative)</strong></summary>

```rego
package kfm.authz

default decision := {
  "decision": "deny",
  "policy_label": input.resource.policy_label,
  "obligations": [],
  "reason_codes": ["DEFAULT_DENY"]
}

decision := out {
  allow
  out := {
    "decision": "allow",
    "policy_label": input.resource.policy_label,
    "obligations": obligations,
    "reason_codes": ["ALLOW_MATCHED_RULE"]
  }
}

allow {
  input.user.role == "steward"
}

allow {
  input.user.role == "public"
  input.action == "read"
  input.resource.policy_label == "public"
}

obligations[o] {
  input.resource.policy_label == "public_generalized"
  o := {"type": "show_notice", "message": "Geometry generalized due to policy."}
}
```
</details>

[Back to top](#top)
