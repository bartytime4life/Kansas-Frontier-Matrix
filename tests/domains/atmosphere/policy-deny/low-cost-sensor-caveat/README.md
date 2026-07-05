<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests/domains/atmosphere/policy-deny/low-cost-sensor-caveat/readme
title: Atmosphere Policy-Deny Test Lane — Low-Cost Sensor Caveat README
type: test-lane-readme
version: v0.1
status: draft
owners:
  - <PLACEHOLDER — Atmosphere steward>
  - <PLACEHOLDER — Policy steward>
  - <PLACEHOLDER — Test steward>
  - <PLACEHOLDER — Evidence/governance reviewer>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
implementation_status: scaffold
verification_status: current-session path verified; implementation not verified
related:
  - tests/README.md
  - tests/domains/atmosphere/README.md
  - tests/domains/atmosphere/policy-deny/README.md
  - docs/doctrine/directory-rules.md
  - docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
  - docs/domains/atmosphere/POLICY.md
  - docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md
  - policy/domains/atmosphere/low_cost_sensor_caveats_required.rego
  - contracts/domains/atmosphere/AirObservation.md
  - fixtures/domains/atmosphere/
  - tools/validators/
tags:
  - kfm
  - tests
  - atmosphere
  - policy-deny
  - low-cost-sensor
  - caveat
  - confidence
  - limitations
  - fail-closed
] -->

<a id="top"></a>

# Atmosphere Policy-Deny Tests — Low-Cost Sensor Caveat

> Test-lane contract for proving KFM keeps low-cost sensor records qualified, caveated, evidence-linked, and separate from uncaveated or higher-authority observation claims.

![status: draft](https://img.shields.io/badge/status-draft-orange)
![lane: tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational](https://img.shields.io/badge/lane-tests%2Fdomains%2Fatmosphere%2Fpolicy--deny-informational)
![rule: caveats--required](https://img.shields.io/badge/rule-caveats--required-red)
![policy: fail--closed](https://img.shields.io/badge/policy-fail--closed-blue)
![implementation: scaffold](https://img.shields.io/badge/implementation-scaffold-yellow)

**Status:** `draft`  
**Authority:** test-lane README; not a schema, policy implementation, validator, source registry, release decision, receipt, proof, or fixture inventory  
**Owning root:** `tests/`  
**Domain segment:** `domains/atmosphere/`  
**Lane:** `policy-deny/low-cost-sensor-caveat/`  
**Default posture:** restrict or deny when required caveat controls are missing  
**Last reviewed:** 2026-07-05

---

## Contents

1. [Purpose](#1-purpose)
2. [Directory fit and authority](#2-directory-fit-and-authority)
3. [Rule statement](#3-rule-statement)
4. [Status and evidence boundary](#4-status-and-evidence-boundary)
5. [What belongs here](#5-what-belongs-here)
6. [What does not belong here](#6-what-does-not-belong-here)
7. [Policy-deny proof matrix](#7-policy-deny-proof-matrix)
8. [Allowed claim boundary](#8-allowed-claim-boundary)
9. [Fixture contract](#9-fixture-contract)
10. [Expected outcomes](#10-expected-outcomes)
11. [Lifecycle gates](#11-lifecycle-gates)
12. [Suggested local commands](#12-suggested-local-commands)
13. [Review burden](#13-review-burden)
14. [Related folders and files](#14-related-folders-and-files)
15. [Open questions](#15-open-questions)
16. [Definition of done](#16-definition-of-done)
17. [Changelog](#17-changelog)
18. [Last reviewed](#18-last-reviewed)

---

## 1. Purpose

This directory is the Atmosphere / Air test sublane for the **low-cost sensor caveat policy-deny / restrict rule**.

It exists to prove that KFM preserves qualification and evidence boundaries for records carrying the `LOW_COST_SENSOR` knowledge character.

A passing suite should support these claims:

1. Required caveat, confidence, correction, and limitation fields remain attached to low-cost sensor records.
2. Missing qualification fields produce a finite denial, restriction, hold, abstention, or validation failure.
3. API, UI, AI, catalog, and graph projections do not strip qualification fields.
4. Derived or corrected products retain lineage from the original candidate record.
5. Test fixtures are local, deterministic, public-safe, and no-network by default.

---

## 2. Directory fit and authority

Directory Rules place enforceability proof under `tests/`. Domain-specific test material uses the domain as a segment inside the responsibility root:

```text
tests/domains/atmosphere/policy-deny/low-cost-sensor-caveat/
```

This path is correct because:

| Placement question | Answer |
|---|---|
| Primary responsibility | Prove a specific Atmosphere policy restriction/denial. |
| Owning root | `tests/` |
| Domain segment | `domains/atmosphere/` |
| Parent lane | `policy-deny/` |
| Sublane | `low-cost-sensor-caveat/` |
| Policy home | `policy/domains/atmosphere/` |
| Validator home | `tools/validators/` |
| Object meaning home | `contracts/domains/atmosphere/` |
| Fixture home | `fixtures/domains/atmosphere/` unless tiny local test-only samples are documented. |
| Release home | `release/` |
| Receipts/proofs home | `data/receipts/` and `data/proofs/` |

> [!WARNING]
> This directory must not become a second policy home. It tests policy behavior; policy definitions stay under `policy/domains/atmosphere/`.

[↑ Back to top](#top)

---

## 3. Rule statement

**Rule:** Low-cost sensor records require governed qualification fields before strong public-facing claims or promotion.

Restrict, deny, hold, or abstain by default when any of the following occur:

- `knowledge_character = LOW_COST_SENSOR` is present but required caveat fields are missing.
- Confidence, uncertainty, correction, calibration, or limitation fields are missing where policy requires them.
- A projected record removes caveat or confidence fields.
- A derived output lacks lineage from the original candidate record.
- A release candidate lacks source role, evidence linkage, review state, or public-release posture.

Allow only when the test subject is explicitly governed as a caveated, corrected, restricted, or otherwise policy-approved object and passes required contract, schema, policy, evidence, and release checks.

---

## 4. Status and evidence boundary

| Item | Status |
|---|---|
| Target README path exists in repo | CONFIRMED in this session before this README update. |
| Directory Rules basis for `tests/domains/<domain>/` | CONFIRMED from current repo doctrine. |
| Parent test root allows policy negative cases | CONFIRMED from `tests/README.md`. |
| Atmosphere file-system plan names `low-cost-sensor-caveat.rego` | CONFIRMED; planning path is marked PROPOSED in the plan. |
| `policy/domains/atmosphere/low_cost_sensor_caveats_required.rego` exists | CONFIRMED; scaffold only in current evidence. |
| Doctrine says `LOW_COST_SENSOR` requires correction/caveats/confidence/limitations for public release | CONFIRMED from current Atmosphere policy/knowledge-character docs. |
| `contracts/domains/atmosphere/AirObservation.md` discusses low-cost sensor caveats | CONFIRMED from current repo evidence. |
| Actual tests in this directory | UNKNOWN in this README. |
| Canonical policy module/file name | NEEDS VERIFICATION due to plan/file-name drift. |
| Canonical object schemas and runtime validator names | NEEDS VERIFICATION. |
| CI job names / pytest markers | NEEDS VERIFICATION. |

This README is a lane contract. It does not claim that the full policy logic, fixtures, validators, schemas, or CI gates are implemented.

---

## 5. What belongs here

This directory may contain:

- README and lane contract material for low-cost sensor caveat tests.
- Tests that reject or restrict records missing required caveat/confidence/limitation fields.
- Tests that verify projection surfaces preserve qualification fields.
- Tests that verify corrected/derived products retain source lineage and caveat fields.
- Tests that call policy/validator implementations from their canonical homes.
- Tests that use deterministic, public-safe invalid fixtures for missing-caveat cases.
- Tiny local test-only examples when they are not reusable fixtures and the reason is documented.

---

## 6. What does not belong here

This directory must not contain:

- Policy implementation files.
- Production validators, correction algorithms, calibration pipelines, or adapters.
- Source fetchers, scrapers, live platform pulls, vendor API calls, or downloaded source caches.
- Raw records, processed datasets, catalog records, triplets, or published layers.
- Real credentials, API keys, service accounts, cookies, signed URLs, private endpoints, or device-owner details.
- Schema, contract, source registry, release, receipt, or proof definitions.
- Reusable fixture inventories that belong under `fixtures/domains/atmosphere/`.
- Tests that run live network calls by default.

[↑ Back to top](#top)

---

## 7. Policy-deny proof matrix

| Scenario | Expected result | Rationale |
|---|---|---|
| LOW_COST_SENSOR record lacks caveat field | `RESTRICT`, `DENY`, or validation failure | Required caveat missing. |
| LOW_COST_SENSOR record lacks confidence/uncertainty | `RESTRICT`, `DENY`, or validation failure | False precision risk. |
| LOW_COST_SENSOR record lacks correction/calibration metadata | `RESTRICT`, `DENY`, or validation failure | Quality pathway unknown. |
| LOW_COST_SENSOR record lacks limitation field | `RESTRICT`, `DENY`, or validation failure | Interpretation boundary missing. |
| Projection omits caveat/confidence text | Trust-state failure or `DENY` | Surface overclaim. |
| Generated answer treats a low-cost sensor value as uncaveated truth | `ABSTAIN`, corrected answer, or `DENY` | Generated language cannot overrule policy. |
| Catalog candidate promotes uncaveated low-cost sensor layer | `DENY` or `HOLD` | Publication gate must fail closed. |
| Corrected product lacks lineage from original reading | `DENY` or `ABSTAIN` | Missing transformation trace. |
| Record is displayed as caveated context with evidence and limitations | Allowed if policy permits | Contextual use with caveats is not overclaiming. |

---

## 8. Allowed claim boundary

A valid public-safe or restricted-release low-cost sensor object should make these visible when required by the governing contract and policy:

| Requirement | Purpose |
|---|---|
| Separate stable ID | Prevents raw/candidate data from becoming a public product by mutation. |
| Sensor/network/source context | Shows where the value came from and what type of source it is. |
| Source role | Prevents primary/corroborating/context/restricted collapse. |
| Knowledge character | Distinguishes `LOW_COST_SENSOR` from other characters. |
| Correction/calibration status | Shows whether the value was adjusted and how. |
| Caveat text | Preserves interpretation limits. |
| Confidence/uncertainty | Prevents false precision. |
| Limitation fields | Shows known constraints. |
| EvidenceRef / EvidenceBundle linkage | Allows cite-or-abstain behavior. |
| Review state | Shows whether release is allowed, restricted, denied, or pending. |
| Release metadata | Provides correction and rollback paths if published. |

Without those controls, the safest result is restriction, denial, hold, or abstention.

---

## 9. Fixture contract

Reusable fixtures should normally live under:

```text
fixtures/domains/atmosphere/
```

Expected fixture families for this lane include:

| Fixture kind | Example purpose |
|---|---|
| Invalid low-cost sensor missing caveat | Proves caveat field is required. |
| Invalid low-cost sensor missing confidence | Proves confidence/uncertainty is required where policy applies. |
| Invalid low-cost sensor missing correction status | Proves correction/calibration state is required. |
| Invalid projection without caveat | Proves projection overclaim fails. |
| Invalid corrected product missing lineage | Proves transformation claims require provenance. |
| Valid caveated low-cost sensor context | Proves qualified contextual use can pass. |
| Valid corrected/reviewed product | Proves a policy-approved product can pass under separate governed identity. |

Fixture records should be deterministic, public-safe, no-network, and visibly test-only or governed fixture data. They must not be raw source payloads or release artifacts.

---

## 10. Expected outcomes

Policy-deny tests should prefer finite, inspectable outcomes:

```text
ANSWER | ABSTAIN | DENY | ERROR
```

Policy/review pipelines may also use review or promotion outcomes such as:

```text
ALLOW | RESTRICT | DENY | HOLD | ERROR
```

| Condition | Preferred outcome |
|---|---|
| Missing caveat/confidence/limitation | `RESTRICT`, `DENY`, `HOLD`, or validation failure. |
| EvidenceRef missing | `ABSTAIN` or validation failure. |
| Policy module missing or ambiguous | `ERROR` in test setup, not silent pass. |
| Fixture missing | Test failure with clear path. |
| Corrected product evidence incomplete | `DENY`, `HOLD`, or `ABSTAIN`. |
| Valid governed caveated product | Allowed only as caveated/reviewed product with separate identity. |

---

## 11. Lifecycle gates

This lane supports the KFM lifecycle but does not move records through it:

```text
RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED
```

| Gate | Low-cost sensor caveat rule |
|---|---|
| RAW | Source payloads remain raw source material; do not publish from this lane. |
| WORK / QUARANTINE | Missing caveats/confidence/correction should remain work/quarantine until resolved. |
| PROCESSED | Processed output must preserve source role, quality, caveat, and evidence lineage. |
| CATALOG / TRIPLET | Catalog/graph projection must preserve caveats and knowledge character. |
| PUBLISHED | Published claims must carry correct identity, caveat, evidence, policy, correction, and rollback. |
| RECEIPTS / PROOFS | Tests may check references but do not store trust-bearing receipts/proofs here. |
| RELEASE | Release decisions remain under `release/`, not `tests/`. |

Publication is a governed state transition. A passing test is not a release approval.

---

## 12. Suggested local commands

> [!NOTE]
> Command names, policy test runners, marker names, and CI job names are **NEEDS VERIFICATION** until checked against the actual repository configuration.

Likely lane check:

```bash
pytest tests/domains/atmosphere/policy-deny/low-cost-sensor-caveat
```

Likely parent policy-deny check:

```bash
pytest tests/domains/atmosphere/policy-deny
```

Possible policy engine check if configured:

```bash
opa test policy/domains/atmosphere tests/domains/atmosphere/policy-deny/low-cost-sensor-caveat
```

Possible repo-wide validation command if implemented:

```bash
python tools/validate_all.py
```

---

## 13. Review burden

Reviewers should be able to answer:

- Does the test fail or restrict when required caveat fields are missing?
- Does the test require confidence/uncertainty, limitation, and correction/calibration status where policy applies?
- Are source role, knowledge character, and evidence visible where required?
- Are projection surfaces prevented from dropping caveats?
- Does the test call policy/validator code from canonical homes rather than reimplementing it here?
- Are fixtures local, deterministic, public-safe, and no-network?
- Are receipts, proofs, release decisions, and source data kept out of this directory?
- Are policy scaffold gaps and filename drift marked NEEDS VERIFICATION rather than hidden?

---

## 14. Related folders and files

| Path | Relationship | Status from current evidence |
|---|---|---|
| `tests/domains/atmosphere/policy-deny/` | Parent policy-deny test lane. | NEEDS VERIFICATION beyond this README. |
| `policy/domains/atmosphere/low_cost_sensor_caveats_required.rego` | Proposed policy scaffold for this denial/restriction. | CONFIRMED present; scaffold only. |
| `policy/domains/atmosphere/low-cost-sensor-caveat.rego` | Planning-name variant from file-system plan. | NEEDS VERIFICATION; planning path confirmed, file presence not verified as canonical. |
| `contracts/domains/atmosphere/AirObservation.md` | Object-meaning contract that discusses low-cost sensor caveats. | CONFIRMED present; implementation depth remains bounded. |
| `contracts/domains/atmosphere/PM25Observation.md` | Specific pollutant observation contract often affected by low-cost source posture. | Present in search results; content not verified in this README. |
| `contracts/domains/atmosphere/OzoneObservation.md` | Specific pollutant observation contract often affected by low-cost source posture. | Present in search results; content not verified in this README. |
| `fixtures/domains/atmosphere/` | Reusable valid/invalid fixture home. | Fixture families for this lane NEED VERIFICATION. |
| `tools/validators/` | Validator implementation home. | Specific module names NEEDS VERIFICATION. |
| `docs/domains/atmosphere/FILE_SYSTEM_PLAN.md` | Planning source naming low-cost sensor caveat policy lane. | CONFIRMED; plan language includes PROPOSED paths. |
| `docs/domains/atmosphere/POLICY.md` | Human-facing policy doctrine naming low-cost sensor caveats. | CONFIRMED in current evidence. |
| `docs/domains/atmosphere/KNOWLEDGE_CHARACTERS.md` | Knowledge-character documentation for `LOW_COST_SENSOR`. | CONFIRMED in current evidence. |

---

## 15. Open questions

| Question | Status | Notes |
|---|---|---|
| Which policy filename is canonical: `low_cost_sensor_caveats_required.rego` or `low-cost-sensor-caveat.rego`? | NEEDS VERIFICATION | The underscored scaffold exists; the hyphenated planning path appears in the file-system plan. |
| What is the canonical policy package name? | NEEDS VERIFICATION | Must align with final OPA/Rego conventions. |
| Which object families may carry `LOW_COST_SENSOR`? | NEEDS VERIFICATION | Likely `AirObservation`, PM2.5, and ozone objects; confirm contracts/schemas. |
| What fields are mandatory: caveat, confidence, limitations, correction, calibration, QA, or method? | NEEDS VERIFICATION | Should be defined by contracts/schemas/policy. |
| Are low-cost sensor records denied, restricted, held, or allowed with warning by default? | NEEDS VERIFICATION | Exact runtime mapping must be tested. |
| Should API/UI/AI trust-state tests live here or in API/UI lanes? | OPEN | This lane may own policy unit tests; UI/API lanes may own surface rendering. |
| Are approved fixtures synthetic, transformed public samples, or source-derived fixture records? | NEEDS VERIFICATION | Prefer public-safe transformed or synthetic fixtures by default. |

---

## 16. Definition of done

This lane is mature when:

- [ ] A canonical low-cost sensor caveat policy module is selected.
- [ ] Tests restrict or deny records missing required caveat/confidence/limitation/correction fields.
- [ ] Tests preserve caveats in API/UI/AI/catalog outputs or delegate those checks to appropriate lanes with links.
- [ ] Tests allow low-cost sensor data only as caveated/reviewed context or a policy-approved corrected product.
- [ ] Fixtures are deterministic, public-safe, no-network, and stored in the governed fixture lane unless test-local.
- [ ] Tests call canonical validators/policies rather than redefining them.
- [ ] CI or local validation exposes the restriction/denial clearly enough for reviewers.
- [ ] Open questions are resolved or tracked in a verification backlog.

---

## 17. Changelog

| Date | Version | Change |
|---|---:|---|
| 2026-07-05 | v0.1 | Initial governed README for the Atmosphere low-cost sensor caveat policy-deny test lane. |

---

## 18. Last reviewed

**2026-07-05** — Initial README scaffold. Target path was present but empty before update. Current evidence confirms the underscored policy scaffold, low-cost sensor caveat doctrine, and AirObservation contract notes; policy implementation depth, canonical module name, tests, schemas, validators, fixtures, and CI enforcement remain **NEEDS VERIFICATION**.

[↑ Back to top](#top)
