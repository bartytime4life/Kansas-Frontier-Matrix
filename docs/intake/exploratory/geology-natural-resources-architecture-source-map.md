<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/geology-natural-resources-architecture-source-map
title: Geology and Natural Resources Architecture - Governed Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - Geology steward; natural-resources steward; intake steward; validation steward
created: 2026-08-02
updated: 2026-08-02
policy_label: public; intake; exploratory; cite-or-abstain; sensitive-location-aware
owning_root: docs/
responsibility: Preserve a reviewable identity and disposition map from the supplied Geology and Natural Resources architecture report to current KFM repository evidence and the bounded resource-class fixture validator implemented from it without promoting report prose, schemas, source claims, classifications, policy, evidence, rights, release, or publication claims into authority.
source_evidence:
  captured_filename: KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf
  source_date: 2026-04-21
  capture_date: 2026-08-02
  sha256: d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51
  byte_count: 142522
  page_count: 42
  extracted_text_lines: 2721
  extracted_text_words: 13272
  extracted_text_bytes: 211656
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  remote_main_snapshot: 9cdfa7decad14becde07d772d0d9c13c00379fd0
  remote_state_verified_at: 2026-08-02
  open_pull_requests_at_verification: 0
related:
  - ./README.md
  - ../README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/geology/README.md
  - ../../../contracts/domains/geology/MineralOccurrence.md
  - ../../../contracts/domains/geology/ResourceDeposit.md
  - ../../../contracts/domains/geology/ResourceEstimate.md
  - ../../../fixtures/domains/geology/resource_class/README.md
  - ../../../tools/validators/domains/geology/validate_resource_class_distinction.py
  - ../../../tests/domains/geology/test_source_role_anti_collapse.py
tags: [kfm, intake, geology, natural-resources, source-map, resource-class, anti-collapse, public-safe-geometry, no-network]
notes:
  - "The PDF is not committed by this change. Its filename and digest preserve attachment identity for later reconciliation."
  - "Page references identify proposal locations in the supplied report; they do not make its schemas, sources, rights, classifications, policy, evidence, or release behavior current or accepted."
  - "This batch adapts only a bounded offline fixture proof. It does not certify a resource or reserve, activate a source, publish locations, promote, release, deploy, or change repository settings."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology and Natural Resources architecture — governed source map

> **Outcome:** The supplied 42-page report is captured as exploratory design
> evidence. Its strongest repository-grounded contribution is a bounded proof
> that mineral occurrence, resource deposit, and resource estimate records must
> remain distinct, and that modeled potential, permits, production records, and
> precise sensitive locations cannot silently become deposit or reserve truth.

> [!IMPORTANT]
> The report proves that these ideas were proposed in the supplied artifact. It
> does not prove source rights, source admission, real resource claims, economic
> viability, reserve classification, regulatory status, policy approval, or
> public-release safety.

## Source identity and review method

| Field | Confirmed value |
|---|---|
| Captured filename | `KFM_Geology_Natural_Resources_Architecture_PDF_Only_Report_2026-04-21.pdf` |
| Source date | `2026-04-21`, supported by the filename and PDF creation metadata |
| Capture and triage date | `2026-08-02` |
| SHA-256 | `d334f43df8fd74f17115cc0f51861cf8238c9cb99d37adaf95f5e4e1655fdf51` |
| Size and page count | `142,522` bytes; `42` pages |
| Extracted text | `2,721` lines; `13,272` words; `211,656` bytes |
| PDF posture | unencrypted; no JavaScript; no form; untagged |
| Repository comparison | `bartytime4life/Kansas-Frontier-Matrix` at `main@9cdfa7decad14becde07d772d0d9c13c00379fd0` |
| Open pull requests at comparison | `0` |

The review extracted the full document, visually inspected the domain-boundary,
schema-index, public-safety, and test-matrix pages, and compared those proposals
with current Geology contracts, schemas, fixtures, validators, tests, workflow,
and directory-governance surfaces.

## Directory Rules and authority basis

| Material | Selected home | Basis |
|---|---|---|
| Exploratory source identity and disposition | `docs/intake/exploratory/` | Human-readable intake evidence. |
| Frozen fixture behavior | `tools/validators/domains/geology/` | Existing per-domain Geology validator inventory. |
| Synthetic positive and negative cases | `fixtures/domains/geology/resource_class/` | Existing domain-fixture responsibility root. |
| Deterministic behavior proof | `tests/domains/geology/` | Existing domain-test responsibility root. |
| CI orchestration | `.github/workflows/domain-geology.yml` | Existing stable workflow identity. |
| Object meaning | existing `contracts/domains/geology/` files | Referenced, not rewritten by the fixture profile. |
| Machine shapes and policy | existing schema and policy roots | Left unchanged because vocabulary and authority questions remain open. |

No new schema, contract, policy, source-registry, evidence, proof, receipt,
release, runtime, data, or publication authority root is created.

## Report map and disposition

| Report pages | Design pressure | Disposition in this batch |
|---:|---|---|
| 7 | Separate observed, interpreted, and modeled knowledge; keep occurrence, deposit, estimate, reserve, permit, and production claims distinct; protect exact resource locations. | `ADAPT / RETAIN` as fixture-only anti-collapse and location-denial behavior. |
| 16 | Positive and negative schema-index expectations for `MineralOccurrence`, `ResourceDeposit`, and `ResourceEstimate`, including scheme/date/method/confidence support. | `ADAPT / RETAIN` as validator findings and exact negative fixtures; no schema migration. |
| 19 | Generalize or redact mineral/resource localities before public use; deny sensitive exact geometry. | `ADAPT / RETAIN` as generalized-county-only fixture support and exact-location denial. |
| 22 | Negative tests for modeled potential as deposit, missing estimate classification, and sensitive exact public geometry. | `ADAPT / RETAIN` in the deterministic test matrix. |
| Remaining pages | Source families, object families, schemas, pipelines, UI, release, and operational proposals. | `CORROBORATIVE / DEFER` pending source rights, ownership, vocabulary, policy, schema-home, and dependency-closure decisions. |

## Repository-grounded reconciliation

At the inspected base, KFM already documented the three object families and
their anti-collapse boundary. The exact executable gap was narrow:

- `validate_resource_class_distinction.py` was a placeholder;
- `test_source_role_anti_collapse.py` was a placeholder;
- the Geology workflow treated every validator and test as held; and
- Geology schemas remain permissive and carry unresolved naming/classification
  questions that this batch must not silently decide.

The implementation therefore freezes a synthetic profile instead of promoting
the report's proposed field model into canonical schemas.

## Implemented bounded slice

The profile accepts only three synthetic pairings:

| Character | Object family | Source role | Bounded claim |
|---|---|---|---|
| `MINERAL_OCCURRENCE` | `MineralOccurrence` | `observed` | reported presence only |
| `RESOURCE_DEPOSIT` | `ResourceDeposit` | `aggregate` | delineated-body context only |
| `RESOURCE_ESTIMATE` | `ResourceEstimate` | `modeled` | modeled quantity with synthetic scheme, method, date, confidence, and assumptions |

It rejects occurrence-as-resource, modeled-potential-as-deposit,
permit-as-deposit, production-as-deposit, estimate-as-observation,
estimate-as-reserve, missing estimate classification support, precise resource
locations, malformed or oversized JSON, duplicate keys, undeclared fields, and
unbounded reference lists. Diagnostics contain stable codes and JSON paths, not
candidate values. All fixture geometry is the non-real generalized county
sentinel `99999`.

## Proof boundary and remaining work

A passing fixture proves only that the frozen profile and its fail-closed
mechanics behaved as tested. It does not prove:

- that the profile vocabulary is canonical;
- that a real occurrence, deposit, estimate, or reserve exists;
- that source rights, evidence, policy, review, or release requirements close;
- that a classification scheme is scientifically, legally, or economically
  accepted; or
- that exact resource locations may be published.

Canonical classification vocabulary, schema hardening, live source admission,
EvidenceBundle resolution, policy evaluation, resource/reserve stewardship,
and UI/release integration remain **PROPOSED / NEEDS VERIFICATION**.

## Rollback and correction

Rollback is a normal revert of the bounded feature commit. It removes the
validator, fixtures, test, workflow wiring, source map, and generated receipt
without changing source, lifecycle, proof, release, or published state.

[Back to top](#top)
