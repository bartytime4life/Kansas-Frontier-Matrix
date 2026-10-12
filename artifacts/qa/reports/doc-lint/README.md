<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/artifacts-qa-reports-doc-lint-readme
title: artifacts/qa/reports/doc-lint/ — Documentation QA Report, Inspection, and Non-Authority Boundary
type: readme; directory-readme; qa-report-output; documentation-lint-report; compatibility-boundary; inspection-contract
version: v0.2
prior_version: v0.1
status: draft; repository-grounded; compatibility-root; transitional; report-payload-not-present; executable-documentation-validators-available; aggregate-doc-lint-producer-not-established; report-schema-not-established; retention-not-established; release-binding-unestablished; non-authoritative
owners: OWNER_TBD — Docs steward · QA/report steward · Documentation-validator steward · Security/privacy steward · CI/artifact-retention steward · Receipt/proof steward · Release/publication steward
created: 2026-07-16
updated: 2026-08-28
policy_label: public-doc; artifacts; qa; docs; lint; metadata; links; citations; document-graph; freshness; generated-output; inspection-only; no-secrets; no-doctrine-authority; no-evidence-authority; no-policy-authority; no-release-authority; correction-aware; rollback-aware
current_path: artifacts/qa/reports/doc-lint/README.md
owning_root: artifacts/
responsibility: Bound non-authoritative documentation-QA report staging, route maintainers to current executable checks, and prevent check or report results from being mistaken for doctrine, evidence, review, release, or publication authority.
truth_posture: cite-or-abstain
authority_effect: none
source_activation_effect: none
lifecycle_effect: none
release_effect: none
deployment_effect: none
promotion_effect: none
publication_effect: none
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: bacb77cfbc04014a2c05da541f9cba8025629068
  target_prior_blob: f32bde7ff4ea4f2a66d7f2a6a573bad82dcce618
  lane_gitkeep_blob: be0c1dfcf616d938fde3480b46688f3a6e7be710
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  link_validator_blob: c5aff503e306709bc193e1b64f934675631dca95
  meta_block_validator_blob: f5dfd61abf95f7f8d424ec7d8db4ed4fb9feae42
  stale_scan_validator_blob: 11a8aa028e68b0ffe5c4e16c225ffba5bacc5b8d
  document_graph_validator_blob: f1160eaa3d5dd4cbf62fce8790cb3185d4fd5a7d
  link_workflow_blob: 7b6c675d879a36d685b19b18fde401fca1bdd00e
  meta_block_workflow_blob: 732879cd8a5aca71ef3c570a0c34c4c389f20e8a
  stale_scan_workflow_blob: 5a94d7c353c4c18c0bcb9a0df45c81a3916f747a
  document_graph_workflow_blob: 636749f75621bf773ac558286789dadb41c47c35
  citation_workflow_blob: 73f1bb4e993a6b3be773235792705ec29c257a01
  control_plane_workflow_blob: ed0d3b50a12931b67cad005cd99433924c829fa3
  docs_build_workflow_blob: 7816e07d66774d2e2b3b80b66d5d3349a1393861
source_lineage:
  - title: KFM Pass 23 + Pass 32 Consolidated Deduplicated Atlas
    source_class: DRIVE_PLANNING_LINEAGE
    use: Candidate documentation-QA ideas only; the atlas explicitly does not establish current repository implementation.
  - title: KFM Repository Workbench
    source_class: NOTION_COORDINATION_ONLY
    use: Current coordination and check-name discovery only; GitHub bytes and exact-head runs remain controlling evidence.
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../../tools/validators/docs/README.md
  - ../../../../tools/validators/docs/link-check/README.md
  - ../../../../tools/validators/docs/meta-block/README.md
  - ../../../../tools/validators/docs/stale-scan/README.md
  - ../../../../tools/validators/docs/document-graph/README.md
  - ../../../../tools/validators/docs/terminology-parity/README.md
  - ../../../../tools/validators/docs/truth-label-lint/README.md
  - ../../../../tools/validators/citation/README.md
  - ../../../../.github/workflows/link-check.yml
  - ../../../../.github/workflows/docs-meta-block.yml
  - ../../../../.github/workflows/docs-stale-scan.yml
  - ../../../../.github/workflows/docs-document-graph.yml
  - ../../../../.github/workflows/citation-validation.yml
  - ../../../../.github/workflows/docs-control-plane.yml
  - ../../../../.github/workflows/docs-build.yml
  - ../../../../data/receipts/README.md
  - ../../../../data/proofs/README.md
  - ../../../../release/README.md
notes:
  - v0.2 corrects obsolete README-only and TODO-only claims after executable documentation validators, tests, and workflows were added.
  - Current checks emit bounded native output or workflow summaries; no aggregate doc-lint report producer, schema, retained payload, or release binding is established.
  - This change documents current repository behavior only and creates no validator, report, receipt, proof, release, deployment, or publication authority.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Documentation QA report boundary

`artifacts/qa/reports/doc-lint/` is the transitional staging lane for generated documentation-QA inspection copies. KFM now has several executable documentation validators and substantive workflows, but it does not have an aggregate `doc-lint` producer that writes a governed report into this directory.

> [!IMPORTANT]
> A passing validator, green workflow, generated summary, or future report proves only its declared assertion for the named scope and revision. It does not establish doctrine, factual truth, evidence sufficiency, policy permission, human review, release, deployment, promotion, publication, or production parity.

**Quick navigation:** [Disposition](#current-disposition) · [Authority](#authority-and-scope) · [Inventory](#current-lane-inventory) · [Checks](#implemented-documentation-checks) · [Commands](#focused-local-commands) · [CI](#hosted-workflow-map) · [Report contract](#aggregate-report-contract) · [Security](#security-and-sensitive-content) · [Maintenance](#maintenance-correction-and-rollback)

## Current disposition

| Capability | Current state | Bounded conclusion |
|---|---|---|
| Lane boundary | `CONFIRMED` | `README.md` and `.gitkeep` retain this report-staging path. |
| Aggregate `doc-lint` payload | `NOT ESTABLISHED` | No tracked report, run manifest, or summary is present. |
| Aggregate producer and schema | `NOT ESTABLISHED` | No dedicated producer, workflow, or report schema was found on the evidence commit. |
| Local link validator | `IMPLEMENTED` | Checks repository-local Markdown file, directory, image, and fragment targets without requesting external URLs. |
| Metadata-block validator | `IMPLEMENTED` | Checks bounded `KFM_META_BLOCK_V2` envelopes and can emit a review-only registry delta. |
| Freshness validator | `IMPLEMENTED` | Performs deterministic, date-pinned stale-document QA with advisory and bounded-required profiles. |
| Document-graph validator | `IMPLEMENTED` | Builds a no-network relationship and reachability projection with optional registry parity. |
| Citation declaration validator | `IMPLEMENTED` | Replays repository-owned synthetic `CitationValidationReport` fixtures; it does not resolve external evidence. |
| Terminology parity | `README-ONLY LANE` | No standalone executable was established at the documented child path. |
| Truth-label lint | `README-ONLY LANE` | No standalone executable was established at the documented child path. |
| Documentation build | `READINESS HOLD` | The workflow fails if a generator appears without an accepted pinned build contract; it does not render or publish docs. |
| Canonical receipt, proof, or release binding | `NOT ESTABLISHED` | Native validator output and workflow summaries remain QA signals only. |

## Authority and scope

Accepted [ADR-0029](../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the exact [Directory Rules v2](../../../../docs/doctrine/directory-rules.md) bytes. Under that placement model:

| Responsibility | Owning surface |
|---|---|
| Authored documentation and doctrine | `docs/` and the applicable responsibility root |
| Validator implementation | `tools/validators/` |
| Validator tests | `tests/validators/` |
| Hosted orchestration | `.github/workflows/` |
| Regenerable QA inspection copies | `artifacts/qa/reports/` |
| Canonical process memory | Accepted receipt and validation-report homes |
| Evidence and proof | `data/proofs/` and governed evidence homes |
| Release, correction, and rollback decisions | `release/` and their accepted accountability objects |

This lane may stage derived, replaceable inspection output. It must not contain authored doctrine, source data, credentials, restricted excerpts, canonical receipts, EvidenceBundles, proof packs, PolicyDecisions, release records, or published products.

```text
document syntax != document meaning
document meaning != factual truth
citation presence != evidence resolution
evidence resolution != policy permission
workflow success != human review
merge != release
release != deployment or publication
```

## Current lane inventory

```text
artifacts/qa/reports/doc-lint/
├── README.md
└── .gitkeep
```

The following representative payload paths were not established at the evidence commit:

- `artifacts/qa/reports/doc-lint/doc-lint-report.json`
- `artifacts/qa/reports/doc-lint/doc-lint-run.json`
- `artifacts/qa/reports/doc-lint/doc-lint-summary.md`
- `.github/workflows/doc-lint.yml`
- `schemas/artifacts/doc-lint-report.schema.json`

Their absence is repository- and revision-scoped. It does not rule out ephemeral local files, CI-only artifacts, historical branches, or external services.

## Implemented documentation checks

| Check | Executable entry point | What it establishes | What it does not establish |
|---|---|---|---|
| Local links and anchors | [`check_links.py`](../../../../tools/validators/docs/link-check/check_links.py) | Bounded local target and fragment resolution; external URLs are counted but not requested. | Target authority, external availability, semantic correctness, or evidence closure. |
| Metadata blocks | [`check_meta_blocks.py`](../../../../tools/validators/docs/meta-block/check_meta_blocks.py) | Parse and consistency findings for scoped metadata; optional review-only registry delta. | Truth, ownership acceptance, or registry authority. |
| Freshness | [`check_stale_docs.py`](../../../../tools/validators/docs/stale-scan/check_stale_docs.py) | Date-pinned freshness and placeholder-review signals. | Factual falsity, automatic deprecation, or permission to delete. |
| Document graph | [`check_document_graph.py`](../../../../tools/validators/docs/document-graph/check_document_graph.py) | Scoped navigation, relationships, backlinks, reachability, and optional registry parity. | Canonicality, governance adoption, or semantic agreement. |
| Citation declaration | [`validate_citation_validation_report.py`](../../../../tools/validators/citation/validate_citation_validation_report.py) | Synthetic declaration-profile conformance. | External lookup, source admission, EvidenceRef resolution, or EvidenceBundle closure. |

The validators use bounded inputs and finite findings. Their current implementations do not create doctrine, edit source Markdown, activate sources, approve policy, or publish output.

## Focused local commands

From the repository root, maintainers can check this document with the current no-network entry points:

```bash
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  artifacts/qa/reports/doc-lint/README.md

python tools/validators/docs/meta-block/check_meta_blocks.py \
  --repo-root . \
  --profile present \
  --format text \
  artifacts/qa/reports/doc-lint/README.md

python tools/validators/docs/stale-scan/check_stale_docs.py \
  --repo-root . \
  --as-of 2026-08-28 \
  --profile advisory \
  --format text \
  artifacts/qa/reports/doc-lint/README.md

python tools/validators/docs/document-graph/check_document_graph.py \
  --repo-root . \
  --entrypoint artifacts/qa/reports/doc-lint/README.md \
  --format text \
  artifacts/qa/reports/doc-lint/README.md
```

The `--as-of` value is explicit because freshness results are time-dependent. Record the exact revision, arguments, output, and exit status when citing a run.

## Hosted workflow map

| Workflow | Current behavior |
|---|---|
| [`link-check.yml`](../../../../.github/workflows/link-check.yml) | Runs focused no-network tests and checks local targets in changed Markdown. |
| [`docs-meta-block.yml`](../../../../.github/workflows/docs-meta-block.yml) | Runs metadata tests and changed-document metadata validation. |
| [`docs-stale-scan.yml`](../../../../.github/workflows/docs-stale-scan.yml) | Runs deterministic freshness tests and scoped stale-document checks. |
| [`docs-document-graph.yml`](../../../../.github/workflows/docs-document-graph.yml) | Tests and validates the bounded documentation graph projection. |
| [`citation-validation.yml`](../../../../.github/workflows/citation-validation.yml) | Tests and replays the synthetic citation declaration profile. |
| [`docs-control-plane.yml`](../../../../.github/workflows/docs-control-plane.yml) | Performs YAML, register-meta-contract, and ADR inventory coherence checks. |
| [`docs-build.yml`](../../../../.github/workflows/docs-build.yml) | Enforces a fail-closed generator-readiness hold; it does not build or publish documentation. |

Hosted success is revision-bound QA evidence. API security skips, pending checks, unrelated failures, and inherited warnings must be reported separately rather than normalized into a pass.

## Aggregate report contract

No current command aggregates the native check results into a `doc-lint` report in this lane. Until a producer is implemented and reviewed:

- do not claim that this directory contains a current repository-wide QA result;
- do not hand-author JSON or Markdown payloads as if they were generated evidence;
- preserve each validator's native scope, outcome, reason codes, and limitations;
- do not infer aggregate success from a subset of green workflows; and
- treat the prior v0.1 manifest and finding shapes as proposal lineage, not current schema authority.

A future producer should define, at minimum:

| Requirement | Minimum boundary |
|---|---|
| Identity | Repository, exact revision, producer version, profile digest, and input digest. |
| Scope | Included and excluded documents, document count, and nonempty-scope guard. |
| Results | Native child outcome, stable finding code, safe location, and bounded message. |
| Execution | Network posture, reference date, locale, timezone, and resource limits. |
| Output | Deterministic serialization, report digest, retention class, and access posture. |
| Trust separation | Explicitly separate inspection output from receipt, proof, policy, review, release, and publication records. |
| Correction | Supersession, invalidation, withdrawal, rerun, and rollback linkage. |

Do not add a tracked payload here until commit/ignore policy, retention, schema placement, CI ownership, and sensitive-diagnostic handling are settled.

## Security and sensitive content

Documentation diagnostics must not expose:

- credentials, tokens, cookies, keys, or secret-bearing URLs;
- private repository, object-store, service, or runner paths;
- unpublished archaeological or cultural locations;
- rare-species coordinates or reverse-engineerable generalization details;
- living-person, DNA, genealogy, land, parcel, private-well, or observer identifiers;
- critical-infrastructure detail not already approved for the report audience; or
- restricted source excerpts or hidden comments.

Prefer a safe path, line or anchor, stable finding code, and redacted-value digest. Unknown rights or sensitivity route to review, redaction, quarantine, or denial; a documentation checker cannot grant rights.

## Failure interpretation

| Outcome | Interpretation |
|---|---|
| `PASS` | The named check passed for its explicit nonempty scope and revision. |
| `WARN` | Reviewable nonblocking findings remain. |
| `FAIL` | A blocking criterion failed; classify it as introduced, inherited, or unrelated. |
| `ERROR` | Tooling or parsing failed; document validity is unknown. |
| `EMPTY_SCOPE` | Nothing intended was checked; do not report a normal pass. |
| `NOT_RUN` | No substantive run occurred. |
| `NOT_APPLICABLE` | The check does not apply to the stated scope. |
| `UNKNOWN` | Available evidence cannot determine the state. |

Reject vacuous runs that match no files, load no rules, suppress all findings, validate only their own output, or treat readiness-hold workflows as substantive content validation.

## Maintenance, correction, and rollback

Re-check this README when any of these change:

- validator entry points, arguments, profiles, or reason codes;
- workflow names, trigger scopes, commands, or artifact handling;
- direct lane inventory or ignore policy;
- report producer, schema, payload name, retention, or consumer;
- receipt, proof, policy, review, release, or publication relationships; or
- Directory Rules classification of `artifacts/`.

If a future payload is invalid, preserve its digest and lineage, mark it stale or superseded, correct the producer or source document, rerun on immutable inputs, and invalidate affected summaries or release references. Do not silently overwrite release-significant inspection history.

This Markdown change has no operational rollback. Before merge, close the draft pull request or delete its feature branch. After an authorized merge, revert the documentation commit or apply a separately reviewed forward correction.

## Open gaps

- Accepted owners and CODEOWNERS remain unverified.
- Aggregate producer, schema, tests, workflow, payload, retention, and consumers remain unestablished.
- Terminology-parity and truth-label-lint remain documentation-only child lanes.
- External-link checking remains separate from the no-network local-link profile.
- Canonical ValidationReport and validation-receipt relationships remain unsettled.
- Branch-protection significance, release blocking, hosting, deployment, and publication are not established by this lane.

## Evidence ledger

| Evidence | Blob | Bounded support |
|---|---|---|
| Prior target README | `f32bde7ff4ea4f2a66d7f2a6a573bad82dcce618` | v0.1 and its obsolete maturity claims. |
| Lane `.gitkeep` | `be0c1dfcf616d938fde3480b46688f3a6e7be710` | Transitional report directory retention. |
| Directory Rules | `fd49a0b83e55cef52c1124281f093e263526898d` | Placement and responsibility boundary. |
| ADR-0029 | `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Adoption of the exact Directory Rules bytes. |
| Link validator/workflow | `c5aff503e306709bc193e1b64f934675631dca95` / `7b6c675d879a36d685b19b18fde401fca1bdd00e` | Executable no-network local-link QA. |
| Metadata validator/workflow | `f5dfd61abf95f7f8d424ec7d8db4ed4fb9feae42` / `732879cd8a5aca71ef3c570a0c34c4c389f20e8a` | Executable scoped metadata QA. |
| Freshness validator/workflow | `11a8aa028e68b0ffe5c4e16c225ffba5bacc5b8d` / `5a94d7c353c4c18c0bcb9a0df45c81a3916f747a` | Executable date-pinned stale-document QA. |
| Document-graph validator/workflow | `f1160eaa3d5dd4cbf62fce8790cb3185d4fd5a7d` / `636749f75621bf773ac558286789dadb41c47c35` | Executable no-network graph QA. |
| Citation workflow | `73f1bb4e993a6b3be773235792705ec29c257a01` | Synthetic declaration-profile validation. |
| Control-plane workflow | `ed0d3b50a12931b67cad005cd99433924c829fa3` | Substantive repository control-plane checks. |
| Docs-build workflow | `7816e07d66774d2e2b3b80b66d5d3349a1393861` | Explicit readiness hold, not documentation generation. |

These blobs establish repository implementation at the evidence commit only. They do not establish current production behavior or future workflow results.

## Changelog

### v0.2 — 2026-08-28

- replaced obsolete README-only and TODO-only maturity claims with current executable-validator and workflow evidence;
- added exact focused commands and bounded failure interpretation;
- preserved the absence of an aggregate `doc-lint` producer, schema, payload, retention policy, and release binding;
- reduced proposal-era boilerplate while retaining authority, security, correction, and rollback limits.

### v0.1 — 2026-07-16

- established the first substantive boundary for the previously empty README;
- recorded the then-current README-only validator and TODO-only workflow state;
- proposed an aggregate report contract without implementing it.

[Back to top](#top)
