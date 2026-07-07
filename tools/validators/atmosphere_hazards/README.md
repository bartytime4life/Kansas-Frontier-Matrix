<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-atmosphere-hazards-readme
title: tools/validators/atmosphere_hazards README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-atmosphere-steward-plus-hazards-steward-plus-docs-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; compatibility-bridge; cross-domain-validator; atmosphere-hazards
owning_root: tools/
responsibility: compatibility and naming bridge for Atmosphere/Air × Hazards validator work, deferring canonical validator scope to tools/validators/air-hazards unless an ADR renames the lane
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../_common/README.md
  - ../air-hazards/README.md
  - ../../../docs/domains/atmosphere/CROSS_LANE_RELATIONS.md
  - ../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../docs/domains/hazards/ARCHITECTURE.md
  - ../../../contracts/domains/atmosphere/
  - ../../../contracts/hazards/
  - ../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../schemas/contracts/v1/hazards/
  - ../../../policy/domains/atmosphere/
  - ../../../policy/domains/hazards/
notes:
  - "This README documents a compatibility bridge, not an independent validator authority."
  - "The currently documented canonical validator lane for this edge is tools/validators/air-hazards/."
  - "Do not duplicate validator logic between air-hazards and atmosphere_hazards. Rename or merge through ADR/migration if the project chooses a single spelling later."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/atmosphere_hazards

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-compatibility--bridge-informational)
![canonical](https://img.shields.io/badge/canonical-air--hazards-blueviolet)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/atmosphere_hazards/` is a compatibility bridge for the Atmosphere/Air × Hazards validator edge. The current canonical validator README is `tools/validators/air-hazards/README.md`.

---

## Purpose

This path exists to prevent naming drift between two natural spellings of the same cross-domain validator lane:

- `air-hazards/`
- `atmosphere_hazards/`

KFM docs use both **Atmosphere/Air** language. Because `tools/validators/air-hazards/README.md` already defines the full cross-domain validator contract, this README does **not** redefine the lane.

The durable KFM question for this bridge is:

> Is this path redirecting maintainers toward the existing Atmosphere/Air × Hazards validator boundary instead of creating a parallel validator authority?

The intended answer is yes.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/atmosphere_hazards/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Canonical validator README | **CONFIRMED** | `tools/validators/air-hazards/README.md` currently holds the full validator contract. |
| Validator executables in this path | **DENY / NEEDS ADR** | Do not add independent validator code here unless an ADR or migration retires `air-hazards/`. |
| Naming decision | **NEEDS VERIFICATION / ADR CANDIDATE** | The project should eventually choose one canonical spelling. |

[Back to top](#top)

---

## Canonical lane

Use this lane for implementation planning and validator scope:

```text
tools/validators/air-hazards/
```

That canonical lane covers checks for:

- smoke, AOD, AQI, weather, advisory, and fire-weather context;
- Atmosphere/Air ownership boundaries;
- Hazards ownership boundaries;
- knowledge-character preservation;
- source-role separation;
- freshness and expiry handling;
- evidence support;
- sensitivity and release-boundary checks.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Canonical Atmosphere/Air × Hazards validator contract | `tools/validators/air-hazards/` |
| Compatibility bridge / naming pointer | `tools/validators/atmosphere_hazards/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Atmosphere/Air domain meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| Hazards domain meaning | `docs/domains/hazards/`, `contracts/hazards/` or accepted contract home |
| Schemas | `schemas/contracts/v1/...` |
| Policy rules | `policy/...` |
| EvidenceBundles and receipts | `data/proofs/`, `data/receipts/` |
| Release records | `release/` |
| Tests and fixtures | `tests/` and `fixtures/` conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **CONFIRMED:** `tools/validators/air-hazards/README.md` exists and carries the full validator boundary.
- **PROPOSED:** this path may remain as an index/bridge while naming is unsettled.
- **NEEDS VERIFICATION:** whether future code, tests, or CI refer to this spelling.
- **DENY:** duplicating validator logic here while `air-hazards/` remains canonical.

[Back to top](#top)

---

## Allowed content here

Allowed content is intentionally small:

- this README;
- migration notes if the lane is renamed;
- deprecation notices if this bridge is removed;
- ADR links that choose the canonical spelling.

Do not place validator implementation, fixtures, generated reports, schemas, policy, source descriptors, receipts, proofs, release records, or public artifacts here while `air-hazards/` remains the canonical lane.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `BRIDGE_OK` | Caller was directed to the canonical validator lane. |
| `CANONICAL_LANE_MISSING` | Expected canonical README or lane is absent. |
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
- [ ] CI references one canonical lane.
- [ ] Documentation links point to the canonical validator contract.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft compatibility bridge for an empty file. |
| Next smallest safe change | Decide whether `air-hazards` or `atmosphere_hazards` is the canonical spelling through ADR or migration note. |
