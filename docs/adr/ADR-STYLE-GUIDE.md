<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9f97d2c5-0e3a-4d0d-9b71-4a9aab2d89b3
title: ADR Style Guide
type: standard
version: v1
status: draft
owners: TBD
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related:
  - docs/adr/
tags:
  - kfm
  - adr
  - governance
notes:
  - Defines how Architecture Decision Records are written, reviewed, and linked to PRs.
[/KFM_META_BLOCK_V2] -->

# ADR Style Guide

*Architecture Decision Records for Kansas Frontier Matrix (KFM): decisions that are evidence-linked, reversible, and CI-enforceable.*

![Status](https://img.shields.io/badge/status-draft-blue)
![Type](https://img.shields.io/badge/type-standard-lightgrey)
![Policy](https://img.shields.io/badge/policy_label-public-brightgreen)
![Applies to](https://img.shields.io/badge/applies_to-docs%2Fadr-orange)

**Owners:** `TBD`  
**Last updated:** `2026-03-01`  
**Directory:** `docs/adr/`

> **TODO (repo wiring):** Add CI badges (build, policy gate, linkcheck) once the badge URLs are known.

## Navigation

- [Why ADRs exist](#why-adrs-exist)
- [When you must write an ADR](#when-you-must-write-an-adr)
- [Normative language and decision tags](#normative-language-and-decision-tags)
- [File and ID conventions](#file-and-id-conventions)
- [ADR structure](#adr-structure)
- [Review and promotion gates](#review-and-promotion-gates)
- [Template](#template)
- [Checklist](#checklist)
- [FAQ](#faq)

---

## Why ADRs exist

KFM is a **governed, evidence-first** system. ADRs are the mechanism that turns “we should…” into:

- a **decision** that can be reviewed,
- a **rationale** that can be audited,
- a **rollback plan** that keeps us reversible,
- and a **set of checks** that can be enforced in CI.

In KFM terms: ADRs prevent “implicit defaults,” and they turn gaps into **governed progress**.

[Back to top](#navigation)

---

## When you must write an ADR

Write an ADR **before** (or in the same PR as) any change that is hard to reverse or affects KFM invariants.

### Required triggers

You **MUST** create/update an ADR when a PR:

- Changes **policy enforcement** behavior (OPA/Rego rules, obligations, “deny-by-default” posture).
- Changes **deterministic identity** (IDs, hashes, canonicalization rules).
- Changes **catalog contract surfaces** (DCAT / STAC / PROV profiles, cross-link rules, EvidenceRef schemes).
- Changes the **trust membrane** boundary (any path that could enable UI/clients to bypass governed APIs).
- Changes **promotion gates** (what blocks publishing, what artifacts must exist, what validates).
- Introduces a new **system-of-record** store or a new class of projections that must be rebuildable.
- Introduces a new **partner/restricted dataset** pathway, new redaction/generalization standards, or new export rules.

### Recommended triggers

You **SHOULD** write an ADR when a PR:

- Introduces a new major dependency (DB, search engine, workflow orchestrator).
- Adds a new data lifecycle pattern (watchers, incremental updates, bitemporal modeling).
- Establishes a new “default” that other teams will copy.

> **TIP:** If you’re unsure, write the ADR. Small ADRs are cheap; accidental governance drift is expensive.

[Back to top](#navigation)

---

## Normative language and decision tags

### RFC-style keywords (required)

This guide uses:

- **MUST** / **MUST NOT**: non-negotiable rules
- **SHOULD** / **SHOULD NOT**: strong recommendations
- **MAY**: optional

### KFM decision tags (required)

Every ADR must clearly label what is:

- **CONFIRMED**: backed by source-of-truth docs or existing repo evidence
- **PROPOSED**: an implementable recommendation we are adopting
- **UNKNOWN** / **DECISION NEEDED**: not verified or not decided yet

**Rule:** Any **UNKNOWN** must include both:

1) a **recommended default path** (so work can continue), and  
2) the **minimum verification step** to convert UNKNOWN → CONFIRMED.

[Back to top](#navigation)

---

## File and ID conventions

### Location

All ADRs live in:

- `docs/adr/`

> **NOTE:** If the repo later adopts a different doc map, keep redirects/links so old ADR URLs remain valid.

### File naming

**Format (PROPOSED standard):**

`ADR-####-short-kebab-case-title.md`

Examples:

- `ADR-0007-evidence-ref-schemes.md`
- `ADR-0012-pmtiles-default-for-public-tiles.md`

**Rules:**

- `####` is a zero-padded sequence number (monotonic).
- Keep the slug short (≤ 6–8 words).
- No dates in filenames (dates belong in metadata).

### Document identity

Each ADR **MUST** include a **MetaBlock v2** at the top (HTML comment, not YAML). The ADR’s `doc_id` is the stable identifier.

**doc_id format:**

`kfm://doc/<uuid>`

Generate once; do not regenerate on edits.

[Back to top](#navigation)

---

## ADR structure

### Required sections

| Section | Required | Purpose |
|---|---:|---|
| **Title + MetaBlock v2** | ✅ | Stable identity, owners, status, policy label |
| **Context** | ✅ | What problem we’re solving; constraints; why now |
| **Decision** | ✅ | The choice we are making (crisp, testable) |
| **Options considered** | ✅ | At least 2 options (including “do nothing”) |
| **Consequences** | ✅ | Tradeoffs, risks, and what changes for users/devs |
| **Rollback plan** | ✅ | How we undo or supersede safely |
| **Impacted invariants & gates** | ✅ | What KFM invariants/gates are affected |
| **Evidence & references** | ✅ | Links to proofs: benchmarks, threat model notes, tests, docs |
| **Minimum verification steps** | ✅ (if any UNKNOWN) | Smallest checks to remove uncertainty |
| **Follow-ups / work items** | ✅ | What needs to be built, and where it will live |

### KFM-specific “impact” questions (use as a checklist)

In **Impacted invariants & gates**, answer what applies:

- **Trust membrane:** Does this change any path between UI/client and storage/DB?  
- **Truth path:** Does this change RAW/WORK/PROCESSED/CATALOG/PUBLISHED responsibilities?  
- **Promotion contract:** Are gates added/removed/tightened? What now blocks promotion?  
- **Catalog triplet:** Are DCAT/STAC/PROV profiles or cross-links changed?  
- **Evidence resolution:** Are EvidenceRef schemes, resolver behavior, or citation gates affected?  
- **Policy labels & obligations:** Do we add/rename labels? Add new obligation types?  
- **Security & privacy:** Any new data exfiltration risk? Any new export/download paths?  
- **Operations:** Any new on-call burden? Any new “kill switch” required?

> **WARNING:** If you can’t explain the impact on **promotion gates** or **policy**, the ADR is not done.

[Back to top](#navigation)

---

## Review and promotion gates

### ADR review workflow

**Minimum workflow (PROPOSED standard):**

1. **Draft** ADR in the same PR that introduces the change (or a preceding PR).
2. Mark `status: draft` in MetaBlock; set `Decision status: Proposed`.
3. Request review from the owning CODEOWNERS group for the affected area (policy, catalogs, API, UI).
4. When accepted:
   - update `Decision status: Accepted`,
   - update MetaBlock `status: review` → `published` as appropriate,
   - ensure any required CI gates exist (or are added in the same PR).

### Linking ADRs to PRs

Every PR that triggers an ADR **MUST** include:

- a link to the ADR file (relative link preferred), and
- a 1–2 sentence “ADR summary” in the PR description.

**Recommended PR snippet:**

```md
### ADR
- ADR: docs/adr/ADR-00XX-short-title.md

### Summary
- Implements the ADR decision: <one sentence>

### Rollback
- <one sentence; link to ADR rollback plan section>
```

[Back to top](#navigation)

---

## Template

Copy/paste this into a new file in `docs/adr/` and fill it in.

> **NOTE:** Keep the MetaBlock v2 as an **HTML comment** (no YAML frontmatter).

```md
<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: ADR-#### <Short Title>
type: adr
version: v1
status: draft
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - <PR link or path>
  - <related ADRs or specs>
tags:
  - kfm
  - adr
  - <domain or subsystem>
notes:
  - <one-line intent>
[/KFM_META_BLOCK_V2] -->

# ADR-####: <Short Title>

**Decision status:** Proposed | Accepted | Superseded | Rejected  
**Date:** YYYY-MM-DD  
**Deciders:** <names/roles>  
**Reviewers:** <CODEOWNERS group or names>

## Context (why we’re here)

- Problem statement:
- Constraints (policy, performance, cost, timeline):
- What changes if we do nothing:

## Decision (the one-liner)

We will:

- <crisp statement>
- <non-goals / out of scope>

### Decision tag

- [ ] CONFIRMED (backed by repo evidence)
- [ ] PROPOSED (we are adopting this standard)
- [ ] UNKNOWN / DECISION NEEDED (needs verification)

## Options considered

### Option A — <name>

- Summary:
- Pros:
- Cons:
- Risks:
- Exit criteria (how we know it’s failing):

### Option B — <name>

- Summary:
- Pros:
- Cons:
- Risks:
- Exit criteria:

### Option C — Do nothing

- What happens:
- Risks:

## Consequences

### Positive

- ...

### Negative / tradeoffs

- ...

### Risks and mitigations

- Risk:
- Mitigation:
- Residual risk:

## Impacted invariants and gates

- Trust membrane impact:
- Promotion contract impact:
- Catalog triplet impact (DCAT/STAC/PROV):
- Evidence resolution impact:
- Policy labels and obligations impact:
- Security/privacy impact:
- Ops/on-call impact:

## Rollback plan

- Rollback trigger:
- Rollback steps:
- Data migration reversal:
- How we prevent partial rollback states:

## Evidence and references

- Benchmarks:
- Threat model notes:
- Policy fixtures/tests:
- Links to specs/docs:

## Unknowns and minimum verification steps

| Unknown | Recommended default | Minimum verification step |
|---|---|---|
| <UNKNOWN> | <default path> | <smallest check> |

## Follow-ups / work items

- [ ] <task> (owner, target PR)
- [ ] <task> (tests/gates)
```

[Back to top](#navigation)

---

## Checklist

Before marking an ADR **Accepted**, confirm:

- [ ] The **Decision** is one paragraph max and is testable.
- [ ] At least **two options** were considered (including do-nothing).
- [ ] **Consequences** include real tradeoffs (not just “pros”).
- [ ] A concrete **rollback plan** exists.
- [ ] Any **UNKNOWN** has a default + minimum verification step.
- [ ] The ADR explicitly names **which invariants and gates** are affected.
- [ ] If policy/catalogs/evidence are impacted, **CI gates** exist or are added.
- [ ] The PR description links the ADR.

[Back to top](#navigation)

---

## FAQ

### “Isn’t this too much process?”

ADRs are the smallest unit of governance that keeps KFM reversible and auditable.

### “How big should an ADR be?”

Aim for 1–3 pages. If it’s longer, move deep detail into appendices or linked docs.

### “What if a decision changes later?”

Do **not** rewrite history. Create a new ADR that **supersedes** the old one and link them both.

---

## Recommended directory contents

```text
docs/adr/
  ADR-STYLE-GUIDE.md
  ADR-0001-example.md
  ADR-0002-...
```

**Acceptable inputs:**

- ADR markdown files following this guide
- Supporting diagrams (small, versioned assets) referenced by ADRs

**Exclusions:**

- Large design docs (place in `docs/architecture/` or equivalent)
- Generated reports or run receipts (place in the appropriate pipeline/run directories)

[Back to top](#navigation)
