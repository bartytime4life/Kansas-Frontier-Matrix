<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-cross-lane-readme
title: tools/validators/cross-lane README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-architecture-steward-plus-policy-steward-plus-evidence-steward-plus-docs-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; compatibility-bridge; cross-lane-validator; four-invariants
owning_root: tools/
responsibility: compatibility and doctrine-name bridge for KFM cross-lane invariant validation, deferring current full validator scope to tools/validators/cross-domain-joins unless an ADR renames the lane
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../cross-domain-joins/README.md
  - ../../../docs/architecture/cross-domain/cross-lane-relations.md
  - ../../../docs/architecture/cross-domain/source-role-anti-collapse.md
  - ../../../docs/architecture/cross-domain/shared-kernel.md
  - ../../../docs/architecture/cross-domain/trust-membrane.md
  - ../../../docs/architecture/cross-domain/multi-domain-placement.md
  - ../../../contracts/crosswalks/
  - ../../../schemas/contracts/v1/
  - ../../../policy/
  - ../../../data/proofs/evidence_bundle/
  - ../../../data/receipts/
  - ../../../release/
notes:
  - "This README documents a compatibility bridge, not an independent validator authority."
  - "The currently documented full validator lane for this edge is tools/validators/cross-domain-joins/."
  - "Doctrine also names a cross-lane validator surface. Do not duplicate logic between cross-lane and cross-domain-joins; resolve spelling through ADR or migration if needed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/cross-lane

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-compatibility--bridge-informational)
![canonical](https://img.shields.io/badge/canonical-cross--domain--joins-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/cross-lane/` is a compatibility bridge for the KFM cross-lane validator surface. The current full validator README is `tools/validators/cross-domain-joins/README.md`.

---

## Purpose

This path exists to prevent naming drift between two natural spellings of the same validator family:

- `cross-lane/`
- `cross-domain-joins/`

KFM architecture doctrine uses **cross-lane** language for joins across domain lanes. The current full validator contract lives in `tools/validators/cross-domain-joins/README.md`, which states the four invariant checks and authority boundary. This README does **not** redefine that lane.

The durable KFM question for this bridge is:

> Is this path redirecting maintainers toward the existing cross-domain join validator boundary instead of creating a parallel validator authority?

The intended answer is yes.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/cross-lane/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Full validator README | **CONFIRMED** | `tools/validators/cross-domain-joins/README.md` currently holds the full validator contract. |
| Validator executables in this path | **DENY / NEEDS ADR** | Do not add independent validator code here unless an ADR or migration retires `cross-domain-joins/`. |
| Naming decision | **NEEDS VERIFICATION / ADR CANDIDATE** | The project should eventually choose one canonical spelling or document both as alias paths. |

[Back to top](#top)

---

## Canonical lane

Use this lane for implementation planning and validator scope:

```text
tools/validators/cross-domain-joins/
```

That full lane covers checks for the four KFM cross-lane invariants:

| Invariant | Meaning |
|---|---|
| Ownership preserved | A join names each side's owning domain and does not transfer object authority. |
| Source role preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles are not collapsed. |
| Sensitivity preserved | The most restrictive applicable posture governs the joined output. |
| EvidenceBundle support | Consequential sides resolve to evidence support before public exposure. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Full cross-domain join validator contract | `tools/validators/cross-domain-joins/` |
| Compatibility bridge / doctrine-name pointer | `tools/validators/cross-lane/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-lane join doctrine | `docs/architecture/cross-domain/cross-lane-relations.md` |
| Domain meaning | each owning domain's docs/contracts lanes |
| Crosswalk/relation contracts | `contracts/crosswalks/` or accepted cross-domain contract homes |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| EvidenceBundles and receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Published public-safe artifacts | `data/published/` |
| Tests and fixtures | `tests/` and fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED:** `tools/validators/cross-domain-joins/README.md` exists and carries the full validator boundary.
- **PROPOSED:** this path may remain as an index/bridge while naming is unsettled.
- **NEEDS VERIFICATION:** whether future code, tests, CI, docs, or policy bundles refer to this spelling.
- **DENY:** duplicating validator logic here while `cross-domain-joins/` remains the full validator lane.

[Back to top](#top)

---

## Allowed content here

Allowed content is intentionally small:

- this README;
- migration notes if the lane is renamed;
- deprecation notices if this bridge is removed;
- ADR links that choose the canonical spelling;
- pointers to the full validator lane.

Do not place validator implementation, fixtures, generated reports, schemas, policy, source descriptors, receipts, proofs, release records, catalog records, graph/triplet records, published artifacts, or public runtime code here while `cross-domain-joins/` remains the full lane.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `BRIDGE_OK` | Caller was directed to the full validator lane. |
| `CANONICAL_LANE_MISSING` | Expected full validator README or lane is absent. |
| `DUPLICATE_AUTHORITY_RISK` | Both lanes contain implementation logic without migration/ADR. |
| `RENAMING_ADR_REQUIRED` | A maintainer wants to change canonical spelling. |
| `ABSTAIN` | Bridge cannot decide safely with available context. |
| `ERROR` | Bridge check could not safely complete. |

[Back to top](#top)

---

## Review checklist

- [ ] This path remains a bridge unless an ADR changes canonical spelling.
- [ ] Implementation logic is not duplicated here.
- [ ] Any future rename includes a migration note and rollback path.
- [ ] CI references one full validator lane.
- [ ] Documentation links point to the full validator contract.
- [ ] The four invariants remain grounded in cross-lane doctrine.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft compatibility bridge for an empty file. |
| Next smallest safe change | Decide whether `cross-lane` or `cross-domain-joins` is the canonical spelling through ADR or migration note. |
