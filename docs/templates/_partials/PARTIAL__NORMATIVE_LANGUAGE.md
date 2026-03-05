<!--
Template partial: Normative language + evidence labels for KFM docs.

Usage:
- Include this partial in any spec/policy/ADR that defines requirements.
- Do NOT add a KFM_META_BLOCK_V2 here (the parent document should own metadata).
-->

## Normative language

This document uses **normative keywords** (ALL CAPS) and **evidence labels** to make requirements clear, enforceable, and auditable.

### Requirement keywords

The keywords below have **special meaning only when written in ALL CAPS**.

#### Keywords and intent

- **MUST / MUST NOT**  
  An absolute requirement / prohibition.

- **SHOULD / SHOULD NOT**  
  A strong recommendation. Deviations are allowed **only** when there is a documented rationale and an explicit compensating control (e.g., an ADR, issue link, or risk acceptance).

- **MAY**  
  Optional behavior. Implementations are free to choose.

> **Style note (KFM):** Prefer **MUST/SHOULD/MAY** over **SHALL** to reduce ambiguity and keep requirements scannable.

#### Enforcement expectations

Normative requirements are only valuable if they are **verifiable**.

- Every **MUST** requirement **SHOULD** have an enforcement hook (examples):
  - a CI check / unit or integration test,
  - a policy-as-code rule,
  - a promotion gate / checklist item with objective pass/fail criteria.
- If a requirement cannot yet be verified mechanically, keep it **PROPOSED** and add an explicit TODO for the enforcement hook.

#### Quick reference table

| Keyword | Meaning | Expected enforcement posture |
|---|---|---|
| MUST | Required | Fail-closed when violated (tests/policy/gates) |
| MUST NOT | Forbidden | Fail-closed when violated (tests/policy/gates) |
| SHOULD | Recommended default | Warn / document exceptions |
| SHOULD NOT | Discouraged | Warn / require rationale if used |
| MAY | Optional | No enforcement required |

---

### Evidence labels

In addition to requirement keywords, KFM docs tag claims and decisions with one of:

- **[CONFIRMED]**  
  Backed by evidence that a reviewer can inspect (e.g., citations, run records, catalogs, test output, or a linked decision record).

- **[PROPOSED]**  
  Intended design or planned behavior that is not yet implemented, validated, or adopted. Should include a pointer to the plan-of-record (issue/ADR/task).

- **[UNKNOWN]**  
  Not verified. Must include the *smallest* next steps needed to resolve uncertainty (so it can become CONFIRMED or be rejected).

#### Minimal pattern

```markdown
- [CONFIRMED] The service MUST reject requests that violate policy. (evidence: <link/id>)
- [PROPOSED] The connector SHOULD support backfills. (plan: <issue/ADR>)
- [UNKNOWN] The dataset license is _____. (verify: check publisher terms + record in catalog)
```

---

### Writing good requirements

Use normative keywords sparingly and make each one testable:

1. **One requirement per bullet.**
2. **Name the actor** (component/role/system) and the action.
3. **Specify the condition and expected outcome** (so a test can be written).
4. **Link to enforcement** (test name, policy rule id, gate/checklist, or runbook step).
5. Avoid ambiguous phrasing like “should probably”, “as needed”, “etc.”, or “in most cases”.

#### Anti-ambiguity rules

- “must” / “should” / “may” in lowercase are plain English; **ONLY ALL CAPS** are normative.
- Avoid relative time words like “currently” or “latest” in requirements; use explicit dates or version identifiers where time matters.
