# `schemas/tests/invalid/domains/` — Domain Invalid Schema Test Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-tests-invalid-domains-readme
title: schemas/tests/invalid/domains/ README
type: readme; compatibility-index; invalid-test-placement-guardrail
version: v0.1
status: draft; domain-invalid-test-parent-index; child-guardrails-present; NEEDS VERIFICATION
updated: 2026-07-04
policy_label: public
tags: [kfm, schemas, tests, invalid, domains, fixtures, compatibility, validation]
[/KFM_META_BLOCK_V2] -->

## Purpose

`schemas/tests/invalid/domains/` is a parent index for domain-specific invalid schema-test guardrails.

This path is documentation-first. It records where invalid schema-test folders exist and where maintainers should look before adding new domain invalid tests.

## Status

| Item | Status |
|---|---|
| README | present |
| Direct child README lanes found in current search | fauna, flora, habitat, hydrology, transport |
| Current role | parent compatibility index |
| Placement | NEEDS VERIFICATION |
| Test execution | NOT RUN |

## Boundary

This directory is not a schema family, fixture authority, policy authority, validator implementation, CI configuration, emitted test-result store, data root, proof root, or release root.

It should not contain canonical domain schemas, real domain records, source-system exports, lifecycle data, EvidenceBundles, proof packs, release records, public map payloads, direct model-runtime output, or validator code while accepted homes remain separate.

A failing or passing invalid test proves only the tested shape behavior. It does not prove evidence truth, source authority, policy approval, sensitivity approval, rights clearance, release readiness, domain truth, or public-safety.

## Current child inventory

| Child path | Status | Notes |
|---|---|---|
| `fauna/README.md` | present | Invalid Fauna schema-test guardrail; fail-closed sensitivity and geoprivacy posture. |
| `flora/README.md` | present | Invalid Flora schema-test guardrail; rare/protected plant and geoprivacy posture. |
| `habitat/README.md` | present | Invalid Habitat schema-test guardrail; model/context/evidence boundary posture. |
| `hydrology/README.md` | present | Invalid Hydrology schema-test guardrail; source-role, evidence, rights, release, and trust-membrane posture. |
| `transport/README.md` | present | Invalid Transport schema-test guardrail; path conflict with Roads / Rail / Trade remains visible. |

## Correct nearby lanes

| Need | Preferred lane |
|---|---|
| Domain schema shape | `schemas/contracts/v1/domains/<domain>/` or an accepted versioned schema lane |
| Domain semantic meaning | `contracts/domains/<domain>/` |
| Invalid domain examples | `fixtures/domains/<domain>/invalid/` or an accepted domain fixture lane |
| Expected outputs or golden cases | `fixtures/domains/<domain>/golden/` where present |
| Schema test code | `tests/schemas/` or accepted project test root |
| Validator implementation | `tools/validators/` |
| Domain policy posture | `policy/domains/<domain>/` or accepted policy lane |
| Release, correction, rollback decisions | `release/` |

## What belongs here

- This README.
- Child README guardrails for domain-specific invalid schema-test placement.
- Migration notes if historical invalid schema tests are discovered here.
- Temporary mirror notes while test and fixture placement is unresolved.

## What does not belong here

- Canonical `.schema.json` files.
- Invalid fixture payloads that should live under `fixtures/domains/<domain>/invalid/` or a family-specific fixture lane unless an accepted migration says otherwise.
- Real source data, source-system exports, lifecycle data, EvidenceBundles, proof packs, receipts, release manifests, public map payloads, public tiles, dashboards, screenshots, generated summaries, or direct model-runtime output.
- Policy rules, policy decisions, rights approvals, sensitivity approvals, release records, emitted validation reports, validator code, runtime code, package code, or API/UI outputs.
- Claims that any domain object is valid, invalid, source-supported, policy-approved, released, public-safe, or domain truth merely because this path exists.

## Compatibility rules

| Rule | Requirement |
|---|---|
| Keep schemas versioned | Domain schemas belong in accepted schema lanes, not in this test index. |
| Keep fixtures in fixtures | Invalid examples belong in fixture roots unless an accepted migration says otherwise. |
| Keep tests out of schemas unless accepted | Executable schema tests should live in accepted test roots unless this path is formally adopted. |
| Preserve domain boundaries | Invalid tests must not collapse source roles, evidence state, model output, observations, public derivatives, and release state. |
| Tests are not publication | Test outcomes do not publish data, authorize display, or approve release. |
| Avoid parallel roots | Do not create duplicate schema, fixture, validator, policy, proof, receipt, or release homes under this path. |

## Validation

```bash
find schemas/tests/invalid/domains -maxdepth 3 -type f | sort
find schemas/contracts/v1/domains -maxdepth 4 -type f 2>/dev/null | sort
find fixtures/domains -maxdepth 4 -type f 2>/dev/null | sort
pytest tests/schemas tests/contract || true
```

Replace `|| true` with fail-closed CI behavior once the relevant test paths are confirmed.

## Open questions

| Question | Status |
|---|---|
| Should `schemas/tests/invalid/domains/` remain as a compatibility parent index or be retired after migration? | NEEDS VERIFICATION |
| Are there historical references that expect invalid schema tests under this path? | NEEDS VERIFICATION |
| Should invalid schema tests be generated from fixture manifests instead of maintained under `schemas/tests/invalid/`? | NEEDS VERIFICATION |
| Which additional domain child lanes should exist here, if any? | NEEDS VERIFICATION |
