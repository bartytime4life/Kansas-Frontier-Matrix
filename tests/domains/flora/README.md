<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-flora-readme
title: Tests — Flora Domain
class: test-readme
status: draft
truth_posture: CONFIRMED path / PROPOSED coverage map / UNKNOWN enforcement completeness
owner: <flora-domain-steward> + <test-steward> + <data-lifecycle-steward>
created: 2026-07-05
updated: 2026-07-05
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/flora/README.md
  - docs/domains/flora/FILE_SYSTEM_PLAN.md
  - docs/domains/flora/DATA_LIFECYCLE.md
  - docs/domains/flora/SENSITIVITY.md
  - docs/domains/flora/SOURCE_REGISTRY.md
  - fixtures/domains/flora/README.md
  - tests/domains/flora/source_descriptor/README.md
  - tests/domains/flora/sensitivity/README.md
  - tests/domains/flora/temporal/README.md
tags:
  - kfm
  - tests
  - flora
  - validation
  - fixtures
  - no-network
  - evidence-closure
  - sensitivity
  - source-descriptor
  - temporal
  - release
notes:
  - "This README is the index and contract for the Flora domain test lane under tests/domains/flora/."
  - "It records intended coverage and test boundaries; executable test coverage remains UNKNOWN until test files and CI runs prove it."
  - "All Flora tests must preserve the trust membrane and lifecycle invariant; tests prove gates, not botanical truth by prose."
[/KFM_META_BLOCK_V2] -->

# Tests — Flora Domain

![status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)
![root](https://img.shields.io/badge/root-tests%2Fdomains%2Fflora-blue?style=flat-square)
![coverage](https://img.shields.io/badge/coverage-PROPOSED-orange?style=flat-square)
![network](https://img.shields.io/badge/network-no--network-success?style=flat-square)
![posture](https://img.shields.io/badge/posture-fail--closed-critical?style=flat-square)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-orange?style=flat-square)
![truth](https://img.shields.io/badge/truth-CONFIRMED%20path%20%2F%20UNKNOWN%20CI-lightgrey?style=flat-square)

> **Purpose.** This directory is the Flora-domain test root. It proves that Flora sources, objects, policy decisions, evidence closure, temporal support, sensitivity handling, release manifests, and rollback drills are enforceable before any Flora material reaches a public surface.

---

## 1. Placement and authority

`tests/domains/flora/` is the canonical domain-specific test lane for Flora. Tests live here because their primary responsibility is **enforceability proof**. Fixtures live under `fixtures/domains/flora/` and must remain no-network by default.

| Question | Answer |
|---|---|
| Owning root | `tests/` |
| Domain segment | `domains/flora/` |
| Fixture counterpart | `fixtures/domains/flora/` |
| Primary placement doc | `docs/domains/flora/FILE_SYSTEM_PLAN.md` |
| Lifecycle doc | `docs/domains/flora/DATA_LIFECYCLE.md` |
| Sensitivity doc | `docs/domains/flora/SENSITIVITY.md` |
| Source registry doc | `docs/domains/flora/SOURCE_REGISTRY.md` |
| Status | Path confirmed by repository presence; coverage map remains PROPOSED until executable tests and CI runs exist. |

**Directory basis.** Directory Rules place enforceability proofs under `tests/` and domain-specific proof lanes under `tests/domains/<domain>/`. The Flora file-system plan lists this root and its expected test sublanes.

---

## 2. What this root proves

The Flora test root should prove KFM's Flora lane can move from source admission to public-safe release without bypassing evidence, policy, sensitivity, time, or rollback gates.

| Proof surface | Required behavior | Failure posture |
|---|---|---|
| Source admission | Flora source descriptors fix identity, role, rights, sensitivity, cadence, access, and citation before activation. | Source not admitted or held for review. |
| Schema and contracts | Flora objects match canonical schema shape and contract meaning. | Schema/contract validation failure. |
| Rights | Unknown, stale, restricted, or incompatible source terms block public derivatives. | `RIGHTS_UNKNOWN`, `TERMS_STALE`, or equivalent. |
| Sensitivity | Rare, protected, culturally sensitive, or join-sensitive material fails closed without review and redaction/generalization. | `SENSITIVITY_UNRESOLVED`, `MISSING_RECEIPT`, or equivalent. |
| Evidence closure | Claims resolve `EvidenceRef -> EvidenceBundle` before public release. | `MISSING_EVIDENCE` or hold at prior state. |
| Temporal support | Source, observed, valid, retrieval, release, and correction times remain distinct where material. | Temporal validation failure or stale state. |
| Geometry and geoprivacy | Generalized/redacted geometry is deterministic, receipt-backed, and policy-approved. | Deny public geometry or hold for review. |
| Citation | Public claims carry source role and citation qualifiers. | Citation validation failure or abstention. |
| Release manifest | Public artifacts have release decision, review state, correction path, and rollback target. | No public edge. |
| Rollback drill | Failed releases can revert to a prior release with visible correction lineage. | Held until rollback is validated. |
| No-network operation | Domain tests run deterministically from fixtures. | Test failure; live dependency rejected. |

---

## 3. Test-lane map

The planned Flora test tree is intentionally split by proof responsibility.

```text
tests/domains/flora/
├── README.md                                # this file
├── schema/                                  # schema validation tests
├── source_descriptor/                       # admission gate tests
├── rights/                                  # rights validator tests
├── sensitivity/                             # rare-plant + join-induced deny tests
├── evidence_closure/                        # EvidenceBundle resolution tests
├── temporal/                                # observed/valid/retrieval/release distinct
├── geometry/                                # generalization + redaction transforms
├── policy_deny/                             # exact sensitive geometry deny
├── citation/                                # citation-validation cases
├── release_manifest/                        # ReleaseManifest checks
├── rollback_drill/                          # rollback test harness
└── no_network/                              # no-live-network fixture pipeline
```

Current README coverage in this lane:

| Lane | README status | Primary concern |
|---|---|---|
| [`source_descriptor/`](./source_descriptor/) | Present | Source admission, source role, rights, sensitivity, cadence, access, citation, descriptor provenance. |
| [`sensitivity/`](./sensitivity/) | Present | Rare-plant geoprivacy, exact-geometry denial, redaction receipts, tier transitions, join-induced sensitivity. |
| [`temporal/`](./temporal/) | Present | Source, observed, valid, retrieval, release, correction time; staleness; temporal joins. |
| `schema/` | PROPOSED | Flora object schema validation. |
| `rights/` | PROPOSED | Rights and terms gate behavior. |
| `evidence_closure/` | PROPOSED | `EvidenceRef -> EvidenceBundle` resolution. |
| `geometry/` | PROPOSED | Geometry validation, generalization, redaction transforms, precision constraints. |
| `policy_deny/` | PROPOSED | Deny-by-policy checks, especially exact sensitive public geometry. |
| `citation/` | PROPOSED | Role-aware citation and public-surface qualifier enforcement. |
| `release_manifest/` | PROPOSED | ReleaseManifest, review state, public-safe artifact checks. |
| `rollback_drill/` | PROPOSED | CorrectionNotice, RollbackCard, derivative invalidation tests. |
| `no_network/` | PROPOSED | Ensures domain tests do not reach live services. |

---

## 4. Fixture discipline

All Flora tests should use fixture data instead of live network calls. The fixture counterpart is:

```text
fixtures/domains/flora/
├── README.md                                # PROPOSED / expected
├── valid/                                   # green-path inputs
├── invalid/                                 # negative cases, one per validator where practical
├── golden/                                  # canonical reference inputs
├── synthetic/                               # synthetic rare-plant and edge-case records
└── plants_drift/                            # PLANTS / taxonomy-drift fixtures
```

Fixture rules:

- Use synthetic or public-safe examples by default.
- Do not include real precise rare-plant coordinates.
- Do not include unpublished steward knowledge, private contacts, credentials, API keys, or restricted source payloads.
- Invalid fixtures should fail for exactly one primary reason where practical.
- Golden fixtures should be stable, small, and reviewable.

---

## 5. Lifecycle gates under test

Flora tests should mirror the governed lifecycle rather than testing public artifacts as loose files.

| Lifecycle transition | Test expectation |
|---|---|
| Admission `— -> RAW` | SourceDescriptor exists and resolves; source role, rights, sensitivity, cadence, citation, and hash are present. |
| Normalization `RAW -> WORK / QUARANTINE` | Transform receipts, working validation, policy decisions, and quarantine reasons are emitted. |
| Validation `WORK -> PROCESSED` | Validators are deterministic and tied to fixtures; redaction/aggregation receipts exist when needed. |
| Catalog closure `PROCESSED -> CATALOG / TRIPLET` | EvidenceRefs resolve; EvidenceBundles and graph/catalog projections close. |
| Release `CATALOG / TRIPLET -> PUBLISHED` | ReleaseManifest, review state, correction path, and rollback target are present. |
| Correction / rollback | CorrectionNotice, RollbackCard, invalidation list, and supersession path are inspectable. |

A test that writes or assumes public exposure without those gates is testing the wrong system behavior.

---

## 6. Minimal acceptance matrix

A first useful implementation of the Flora test root should include at least these executable scenarios:

| ID | Scenario | Owning lane |
|---|---|---|
| `FLORA-TEST-001` | Valid source descriptor passes generic and Flora-specific admission checks. | `source_descriptor/` |
| `FLORA-TEST-002` | Candidate or rights-unknown source cannot publish. | `source_descriptor/`, `rights/` |
| `FLORA-TEST-003` | Exact rare-plant geometry is denied on public surfaces. | `sensitivity/`, `policy_deny/` |
| `FLORA-TEST-004` | Public-safe rare-plant derivative requires RedactionReceipt and ReviewRecord. | `sensitivity/`, `geometry/` |
| `FLORA-TEST-005` | Observed time, retrieval time, release time, and correction time remain distinct. | `temporal/` |
| `FLORA-TEST-006` | EvidenceRef fails closed when EvidenceBundle is missing. | `evidence_closure/` |
| `FLORA-TEST-007` | Public claim citation includes source role qualifier where needed. | `citation/` |
| `FLORA-TEST-008` | ReleaseManifest blocks release without rollback target. | `release_manifest/` |
| `FLORA-TEST-009` | Rollback drill reverts a failed release and records correction lineage. | `rollback_drill/` |
| `FLORA-TEST-010` | No-network guard catches live source/API access. | `no_network/` |

---

## 7. Non-goals

This test root must not:

- call live external source APIs;
- store source data, credentials, API keys, or private steward contacts;
- publish or normalize real exact rare-plant coordinates as fixtures;
- treat test prose as proof that enforcement exists;
- bypass the governed lifecycle to assert public exposure;
- create parallel schema, policy, source-registry, fixture, receipt, or release homes;
- infer source role, sensitivity tier, or rights posture using AI output; or
- silently convert `DENY`, `HOLD`, `ABSTAIN`, or `ERROR` into a passing empty result.

---

## 8. Review checklist

Before adding or changing Flora tests, confirm:

- [ ] The test belongs under the correct sublane.
- [ ] The fixture is synthetic, public-safe, or intentionally invalid.
- [ ] The test is deterministic and no-network.
- [ ] The expected result is fail-closed when evidence, policy, rights, sensitivity, temporal support, receipt, or review state is missing.
- [ ] The test preserves the RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED lifecycle.
- [ ] The test uses governed interfaces or validators rather than reading internal stores as public truth.
- [ ] The test records finite, inspectable outcomes and reason codes.
- [ ] Any path conflict is filed as drift or verification backlog, not silently normalized.

---

## 9. Current implementation note

This root README is documentation-first. The repository now has README coverage for `source_descriptor/`, `sensitivity/`, and `temporal/`, but executable test coverage, fixtures, validator implementation, and CI wiring remain `UNKNOWN` until verified by actual files and validation runs.

---

## 10. Definition of done

This Flora test root becomes implementation-backed when:

- every sublane listed in the test-lane map has either executable tests or a README explaining why it is deferred;
- fixtures exist under the approved Flora fixture home and contain no sensitive real coordinates;
- source descriptor, sensitivity, temporal, evidence, citation, release, rollback, and no-network tests run in CI;
- failures emit finite, inspectable outcomes rather than silent skips;
- every public-surface test goes through governed release or API behavior; and
- the test root is linked from Flora domain docs and the repository validation index.
