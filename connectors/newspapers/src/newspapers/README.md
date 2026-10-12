<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://connectors/newspapers/src/newspapers/readme
title: Newspaper Connector Python Package
path: connectors/newspapers/src/newspapers/README.md
type: connector-package-readme
version: v0.2
prior_version: v0.1
prior_blob: b725cf66a235d03037829592b1a2be31a8d2b057
base_commit: af951ea2b4991f6b5fb66ac47ad16bbad587b49f
status: draft
owners: OWNER_TBD — source steward · connector steward · archives steward · genealogy steward · people-dna-land steward · settlements steward · validation steward · data steward · rights steward · sensitivity steward
created: 2026-06-19
updated: 2026-07-14
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: connectors/
lifecycle_phase: source-admission
source_family: newspapers
package_name: newspapers
distribution_name: kfm-connector-newspapers
related:
  - ../../README.md
  - ../README.md
  - ../../tests/README.md
  - ../../../README.md
  - ../../../../docs/sources/catalog/newspapers/README.md
  - ../../../../docs/sources/catalog/newspapers/ocr-full-text.md
  - ../../../../docs/sources/catalog/newspapers/event-reporting.md
  - ../../../../docs/sources/catalog/newspapers/legal-notices.md
  - ../../../../docs/sources/catalog/newspapers/obituaries.md
  - ../../../../docs/sources/catalog/loc/README.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../data/registry/sources/README.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../fixtures/README.md
tags:
  - kfm
  - connectors
  - newspapers
  - python-package
  - archives
  - ocr
  - iiif
  - genealogy
  - settlements
  - privacy
  - source-admission
  - raw
  - quarantine
  - rights-review
notes:
  - "At the pinned base, the package contains this README and an empty __init__.py; proposed runtime modules are not implemented."
  - "The distribution metadata is a greenfield 0.0.0 placeholder; installability and public imports are unverified."
  - "Neighboring source-root and tests READMEs exist, but dedicated test modules and newspaper fixtures did not surface."
  - "Newspaper source-catalog and product pages exist; they are draft documentation and do not activate this package."
  - "OCR, extraction, person/event/place resolution, rights, privacy, sensitivity, proof, release, and publication authority remain outside this package."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Newspaper connector Python package

Implementation boundary for newspaper source-admission code under `connectors/newspapers/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: empty package" src="https://img.shields.io/badge/implementation-empty%20package-lightgrey">
  <img alt="Version: 0.0.0 placeholder" src="https://img.shields.io/badge/version-0.0.0%20placeholder-lightgrey">
  <img alt="Output: RAW or QUARANTINE only" src="https://img.shields.io/badge/output-RAW%20%7C%20QUARANTINE-orange">
  <img alt="OCR: derived candidate" src="https://img.shields.io/badge/OCR-derived%20candidate-orange">
  <img alt="Rights and privacy: fail closed" src="https://img.shields.io/badge/rights%20%2F%20privacy-fail%20closed-red">
</p>

> [!CAUTION]
> This package may eventually fetch, parse, preserve, and route newspaper source material. It is not newspaper truth, authoritative transcription, entity/person/event/place truth, genealogy truth, rights or privacy policy, SourceDescriptor authority, schema authority, proof or receipt authority, release authority, a public API, or generated-answer evidence.

---

## Quick contract

| Question | Answer |
|---|---|
| What is implemented now? | An empty `__init__.py` and documentation. No runtime module or public import surface was verified. |
| What is the package version? | `0.0.0` in a greenfield-placeholder `pyproject.toml`; release/install readiness is not implied. |
| Is live source access implemented or enabled? | **No verified implementation or activation.** |
| What may future package code emit? | Bounded admission material for `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/<domain>/<source_id>/<run_id>/` only. |
| Is OCR authoritative text? | **No.** Preserve the page artifact, raw OCR, engine/run identity, quality, and uncertainty separately. |
| Are names, dates, places, relationships, or events facts? | **No.** Extraction results are candidates until downstream resolution and evidence closure. |
| Does public availability clear copyright, privacy, or reuse? | **No.** Source/product/use-specific review is required. |
| Can UI or AI read package/RAW output directly? | **No.** Public surfaces consume governed released artifacts only. |

---

## Verified repository state

The table records observations at base commit `af951ea2b4991f6b5fb66ac47ad16bbad587b49f`. Expected-path probes and targeted search show what surfaced during this update; they are not exhaustive proof that no other file exists.

| Surface | Observed state | Consequence |
|---|---|---|
| This README | Existing v0.1 at blob `b725cf66a235d03037829592b1a2be31a8d2b057`. | v0.2 replaces unknown inventory claims with pinned evidence. |
| [`connectors/newspapers/README.md`](../../README.md) | Parent connector-family boundary exists and remains draft/placement-unratified. | This package inherits RAW/QUARANTINE-only and no-publication rules. |
| [`connectors/newspapers/src/README.md`](../README.md) | Source-root README exists. | It documents the source tree; it does not prove code. |
| [`connectors/newspapers/tests/README.md`](../../tests/README.md) | Test-lane README exists. | It defines proposed tests/fixtures, not passing coverage. |
| `connectors/newspapers/pyproject.toml` | Greenfield placeholder with distribution `kfm-connector-newspapers`, version `0.0.0`. | Build/install/dependency/entry-point behavior remains unverified. |
| `__init__.py` | Exists as the empty Git blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`. | No public imports or import-time behavior are implemented at the pinned base. |
| `config.py`, `client.py`, `parser.py`, `ocr.py`, `iiif.py`, `extraction.py`, `sensitivity.py`, `envelope.py`, `errors.py` | Absent at the expected package paths. | Their contracts below are proposed activation requirements, not implemented APIs. |
| Expected connector-local test modules | Absent at the checked paths; no `test_newspapers` result surfaced. | No package test coverage is claimed. |
| Newspaper-specific fixtures | No payload fixture surfaced in targeted search. | Fixture design remains proposed; fixture docs elsewhere are not payload evidence. |
| [`docs/sources/catalog/newspapers/README.md`](../../../../docs/sources/catalog/newspapers/README.md) | Dedicated newspaper source-family profile exists, with product pages for OCR, event reporting, legal notices, and obituaries. | Product distinctions are documented but remain draft and non-activating. |
| [`docs/sources/catalog/loc/README.md`](../../../../docs/sources/catalog/loc/README.md) | LOC source-family catalog exists and references newspaper/Chronicling America lineage. | LOC doctrine remains outside this connector package. |
| Expected newspaper/ChronAm SourceDescriptor instances | None surfaced at checked `data/registry/sources/` paths. | Live activation is not established. |
| SourceDescriptor schemas | `source_descriptor.schema.json` exists; a separate `source-descriptor.json` is a proposed placeholder. | Schema-home/filename drift is outside this package; use only the accepted validator path. |
| `.github/CODEOWNERS` | No newspapers-specific ownership rule surfaced. | Owners remain `OWNER_TBD`. |

> [!IMPORTANT]
> Empty package scaffolding plus prose is not an implementation. This README intentionally separates verified files from the future contract so code, tests, descriptors, rights decisions, and activation cannot be inferred from directory presence.

---

## Placement and package boundary

Directory Rules §7.3 confirms `connectors/` as the source fetch/admission root and limits connector output to RAW or QUARANTINE. It does not ratify `connectors/newspapers/` in its example spine or define this exact Python `src/` layout.

Treat this path as:

- **CONFIRMED repository path** — the package directory, README, and empty `__init__.py` exist;
- **CONFIRMED responsibility fit** — future newspaper fetch/parse/admit code belongs under a connector responsibility root;
- **PROPOSED package layout** — `src/newspapers/` is supported by local scaffolding but not proven buildable;
- **non-authoritative** — this README cannot settle connector placement, packaging, schema, policy, or lifecycle authority.

Do not create parallel `connectors/newspaper/`, `connectors/chronam/`, top-level `newspapers/`, or domain-owned fetch packages to work around placement questions. Resolve relocations through an ADR or migration note with import redirects, owner review, and rollback instructions.

Package-local code may own:

- source-specific request construction after activation;
- transport response handling and bounded retries;
- newspaper/issue/page/article/clipping/image/OCR parsing;
- immutable provenance and digest preparation;
- product-aware admission-envelope construction;
- finite connector errors and quarantine reasons.

It may not own:

- source-family or domain doctrine;
- canonical SourceDescriptor/schema/policy definitions;
- authoritative OCR correction, entity resolution, relationship resolution, or event adjudication;
- downstream normalization, catalog/triplet construction, proof closure, redaction receipts, release decisions, publication, UI, or AI answers.

---

## Current and proposed module inventory

| Module | Current state | Future bounded responsibility |
|---|---|---|
| `__init__.py` | **CONFIRMED empty** | Eventually expose a small, stable, side-effect-free public import surface. |
| `config.py` | **ABSENT / PROPOSED** | Parse explicit connector configuration and activation flags without reading secrets at import. |
| `client.py` | **ABSENT / PROPOSED** | Execute an approved source request with finite timeout, retry, paging, rate-limit, and no-network controls. |
| `parser.py` | **ABSENT / PROPOSED** | Preserve upstream newspaper/product structure and create candidate admission records without asserting truth. |
| `ocr.py` | **ABSENT / PROPOSED** | Keep raw OCR, transcription corrections, engine/version/run, confidence, layout, and uncertainty distinct. |
| `iiif.py` | **ABSENT / PROPOSED** | Preserve manifest/canvas/image-service identity, sequence, dimensions, regions, rights, and digests where applicable. |
| `extraction.py` | **ABSENT / PROPOSED** | Emit names, dates, places, relationships, events, and article segments as reviewable candidates with tool/run lineage. |
| `sensitivity.py` | **ABSENT / PROPOSED** | Produce package-local risk signals; canonical policy decisions remain in `policy/`. |
| `envelope.py` | **ABSENT / PROPOSED** | Build a bounded RAW/QUARANTINE handoff with source, product, rights, sensitivity, role, and digest metadata. |
| `errors.py` | **ABSENT / PROPOSED** | Define finite, secret-safe failure classes/codes for callers and tests. |

Do not add a module merely to satisfy this table. Add it with an accepted responsibility, tests, fixtures, and no competing home. If the implementation chooses fewer modules, update this README rather than preserving a fictional architecture.

---

## Import and runtime safety

The current empty `__init__.py` contains no verified import-time network, filesystem, environment, or credential access. Package installability and import execution were not tested from the remote-only workspace.

Future import/runtime rules:

| Concern | Required behavior |
|---|---|
| Import | Importing `newspapers` performs no network call, credential lookup, cache mutation, source activation, file write, or logging setup. |
| Network | Disabled in unit tests and dry runs unless an explicit approved live mode exists. |
| Credentials | Passed at call/runtime boundary through approved secret handling; never required for import or fixture parsing. |
| Timeouts/retries | Finite and configuration-bound; retry state is inspectable and never converts partial results into success. |
| Rate limits | Preserve provider headers/state; stop or quarantine rather than evade upstream limits. |
| Cache | Content-addressed or run-scoped; no silent overwrite of source artifacts. |
| Writes | Restricted to a resolved RAW/QUARANTINE handoff controlled by the caller. |
| Logs | Structured and secret-safe; no full copyrighted OCR dump or sensitive-person/location detail. |
| Publication | Impossible from this package. |

Any future live flag name must be defined by accepted package/repository configuration and tested. The v0.1 example `KFM_ALLOW_LIVE_NEWSPAPER_TESTS` was illustrative and is not claimed as implemented configuration.

---

## Product separation and source roles

Newspaper artifacts are not one semantic product. At minimum keep separate:

| Product | Preserve separately | Anti-collapse rule |
|---|---|---|
| Page/image artifact | Provider, collection/publication, issue/date/edition, page/sequence, image/manifest identity, rights, retrieval, digest. | The page is a source artifact, not proof that every printed statement is true. |
| OCR full text | Page linkage, OCR engine/version/run, raw text, layout/regions, confidence/quality, language/script, digest. | OCR is a derived reading, not authoritative transcription or the page itself. |
| Corrected transcription | Correction method, reviewer/tool, changed spans, source OCR/page refs, correction receipt. | Never overwrite raw OCR; correction still does not adjudicate reported facts. |
| Article/clipping segment | Page/region linkage, segmentation method, headline/byline when present, boundaries, source identifiers. | A segment is not a resolved event/person/place claim. |
| Event reporting | Exact wording/context, publication/time, article/page refs, extraction lineage, ambiguity and contradiction. | A report is not direct observation of the event unless downstream evidence supports that role. |
| Legal notice | Issuing/publishing body, notice type, jurisdiction, publication dates, page/region, legal-source cross-reference. | Printed notice is not automatically final title, court, election, or regulatory truth. |
| Obituary | Publication/date/page, attributed submitter/source when available, extracted assertions and uncertainty. | Family-submitted claims and relationships remain candidates pending corroboration. |
| NER/event extraction | Tool/model/config/run, inputs, spans, confidence, candidates, abstention/review state. | Generated extraction is not source evidence by itself. |

The canonical source-role enum is:

`observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`

Assign roles per admitted product and intended claim in the SourceDescriptor. Do not hardcode a family-wide role. Draft product pages use terms such as `observation`; that is not the canonical enum value `observed`, and the correct role for OCR versus page artifacts remains an admission/ADR question. Until resolved, preserve product identity and quarantine rather than coercing a role.

---

## Admission envelope

Every future successful or quarantined parse should preserve these field groups:

| Field group | Minimum content |
|---|---|
| Source identity | Stable `source_id`, provider, collection, source surface/product, access tier, SourceDescriptor reference, and source role. |
| Request identity | Method/path or local-artifact reference, parameters/body digest, query, page/job/cursor identity, retry lineage, and redacted URL. |
| Publication identity | Newspaper title, edition when available, issue date, volume/number, page/sequence, article/clipping/segment identity, and upstream identifiers. |
| Media identity | Page image/manifest/canvas/image-service reference, region/bounding box, dimensions, media type, and content digest where applicable. |
| OCR/transcription | Raw OCR, engine/version/run, quality/confidence, language/script, layout refs, correction state, and text digest. |
| Extraction | Tool/model/config/run, input refs, spans, candidate type/value, confidence, ambiguity, abstention, and review state. |
| Rights/citation | Product/collection terms, rights statement, copyright/reuse status, citation/attribution, excerpt limits, intended use, reviewer, and re-review trigger. |
| Privacy/sensitivity | Living-person/minor/medical/legal/crime/reputational/cultural/tribal/sacred/burial/archaeology/exact-location signals and decision reference. |
| Retrieval | Retrieval time, upstream/source time, response status, media type, parser/package version, payload/reference digest, fixture/live status. |
| Routing | Owning domain, RAW/QUARANTINE destination, run ID, split-package lineage, decision reason, and quarantine code. |
| Failure | Finite error code, safe detail, retryability, partial state, and steward disposition. |

Never place credentials, cookies, signed URLs, private archive exports, unbounded copyrighted OCR, or sensitive person/location content in logs, exceptions, fixtures, PRs, or public receipts.

---

## OCR, correction, and extraction rules

1. Preserve the page/image artifact independently of OCR.
2. Preserve raw OCR independently of corrected transcription.
3. Pin OCR engine/version/config/run and confidence/quality when known; use `UNKNOWN`, not invented metadata, when absent.
4. Corrections must be span-level or otherwise inspectable and link back to raw OCR and page evidence.
5. Article/clipping segmentation must preserve page context and method/run identity.
6. Extracted people, organizations, places, dates, relationships, events, and quotations remain candidates.
7. Conflicting reports remain separate source assertions; the package does not reconcile them into truth.
8. Search relevance, OCR match, or model confidence is not an evidence score or release decision.
9. Generated summaries remain downstream carriers and must cite released evidence; they do not become inputs to this package as authority.

---

## Rights, privacy, and sensitivity

Public discoverability does not equal permission to download, retain, reproduce, transform, quote, redistribute, or publish. Review is required per provider, collection, item/product, access method, intended use, audience, and excerpt/derivative class.

Fail-closed cases include:

- unknown copyright, rights statement, license, platform/API terms, provider authority, citation, or excerpt limits;
- living-person or minor content;
- medical, legal, crime, abuse, reputational, adoption, parentage, or other family-sensitive claims;
- private address/contact/identity data or account-derived material;
- tribal, sacred, burial, archaeology, culturally restricted, or repatriation-sensitive material;
- exact locations that could expose people, sites, graves, collections, or vulnerable resources;
- a join that creates sensitivity not visible in an individual record;
- long OCR/article excerpts without explicit reuse approval.

The package may preserve risk signals and propose a quarantine reason. Canonical allow/deny/restrict/abstain decisions, redaction/generalization, proof, and release occur outside this package.

---

## Finite outcomes and proposed errors

Runtime outcomes must be finite and inspectable:

`ADMIT_RAW | QUARANTINE | DENY | ABSTAIN | RETRYABLE_ERROR | TERMINAL_ERROR`

These names are a proposed package contract, not current code. If implemented, error classes/codes should cover:

| Proposed code | Condition | Safe outcome |
|---|---|---|
| `missing_source_descriptor` | No complete/current descriptor or activation reference. | DENY or QUARANTINE. |
| `live_access_disabled` | Network access requested outside approved live mode. | DENY without attempting request. |
| `rights_review_required` | Rights/citation/reuse/provider conditions unresolved. | QUARANTINE or ABSTAIN. |
| `privacy_review_required` | Living-person/minor/family-sensitive risk unresolved. | QUARANTINE or DENY. |
| `sensitivity_review_required` | Cultural, tribal, burial, archaeology, or exact-location risk unresolved. | QUARANTINE or DENY. |
| `malformed_source_payload` | Payload is incomplete, ambiguous, or unsupported. | QUARANTINE or terminal error with digest. |
| `ocr_provenance_missing` | OCR lacks required page/engine/run/quality provenance. | QUARANTINE; never silently treat as transcription. |
| `partial_retrieval` | Paging/job/media retrieval is incomplete. | Retry boundedly or quarantine the whole package. |
| `admission_envelope_invalid` | Output cannot satisfy RAW/QUARANTINE envelope/schema requirements. | Terminal error; no fallback write. |

Error messages must not contain secrets, private URLs, full OCR/article text, or sensitive person/location detail.

---

## Test and fixture contract

[`connectors/newspapers/tests/README.md`](../../tests/README.md) documents the intended local guardrails. At the pinned base, expected test modules and newspaper fixture payloads did not surface, so every item below is required future evidence rather than current coverage.

Minimum no-network fixture families:

- synthetic valid page/image + OCR admission;
- missing/invalid SourceDescriptor and activation;
- unknown/restricted rights and citation;
- empty, malformed, partial, paged, duplicate, and drifted source responses;
- OCR without page linkage, engine/run, quality, language, or digest;
- corrected transcription that attempts to overwrite raw OCR;
- ambiguous segmentation and conflicting article reports;
- extraction candidates with missing tool/run/span/confidence/review metadata;
- living-person, minor, medical/legal/crime/reputational, family-sensitive, tribal/cultural, sacred/burial, archaeology, and exact-location risks;
- secret-bearing headers/URLs/errors;
- attempted writes outside resolved RAW/QUARANTINE run paths;
- public/UI/AI shortcut attempts.

Minimum assertions:

- import and fixture parsing require no network or credentials;
- package code cannot activate without a complete descriptor and decision;
- page, OCR, correction, article, and extraction products remain distinct;
- original identifiers, provider, collection, issue/page/article, retrieval, rights, sensitivity, source role, and digests survive;
- failures are finite, secret-safe, and do not produce partial success;
- output targets only RAW or QUARANTINE;
- no connector code creates processed/catalog/triplet/published/proof/receipt/release/API/UI/AI authority.

Use `tests/fixtures/` for deterministic test-only payloads or another accepted test-local location. Use [`fixtures/`](../../../../fixtures/README.md) only for reviewed runtime/synthetic corpora consistent with its root contract. Do not duplicate one fixture corpus across competing homes.

---

## Activation gates

Keep runtime behavior absent or disabled until all applicable gates close:

- [ ] Package placement, owners, distribution/build configuration, and public import surface are accepted.
- [ ] Actual modules replace the proposed inventory and remain import-side-effect-free.
- [ ] A complete SourceDescriptor and SourceActivationDecision exist for every source surface/product/access tier.
- [ ] Source roles use the canonical enum and are resolved per product/claim.
- [ ] Provider terms, rights, citation, excerpt limits, privacy, sensitivity, retention, deletion, and intended-use decisions are current.
- [ ] Network, timeout, retry, paging/cursor/job, rate-limit, caching, and drift behavior are implemented and tested.
- [ ] Page/image, OCR, correction, segmentation, and extraction provenance is lossless and hash-bound.
- [ ] Finite failure codes and secret-safe logging are implemented.
- [ ] Valid/invalid/sensitive/partial/drift no-network fixtures and tests exist.
- [ ] Output escape and public-shortcut tests prove RAW/QUARANTINE-only behavior.
- [ ] Rollback disables activation without deleting descriptor, RAW, quarantine, receipt, proof, correction, or release history.

---

## Evidence and change ledger

| Claim | Status | Evidence / limit |
|---|---|---|
| The package path exists. | **CONFIRMED** | README plus empty `__init__.py` at the pinned base. |
| Runtime modules are implemented. | **DENY** | Only the empty initializer surfaced; named modules were absent at expected paths. |
| The distribution is release-ready. | **DENY** | `pyproject.toml` is a greenfield `0.0.0` placeholder. |
| Dedicated package tests exist and pass. | **UNKNOWN / not surfaced** | Tests README exists; expected test modules and `test_newspapers` results did not surface. |
| Newspaper fixture payloads exist. | **UNKNOWN / not surfaced** | Targeted search surfaced fixture guidance, not a dedicated payload corpus. |
| Newspaper source-family/product docs exist. | **CONFIRMED** | Newspaper catalog README and four product pages exist; all are draft documentation. |
| A complete active newspaper SourceDescriptor exists. | **NEEDS VERIFICATION** | No checked newspaper/ChronAm descriptor path existed. |
| OCR is authoritative transcription. | **DENY** | It is a derived reading that must retain run/provenance/uncertainty and page linkage. |
| Extraction candidates are person/event/place truth. | **DENY** | Downstream evidence resolution and policy review are required. |
| Public availability implies release permission. | **DENY** | Rights/privacy/sensitivity are product/use-specific. |
| Package output is public-ready. | **DENY** | Connector output is limited to RAW/QUARANTINE admission. |

### What changed from v0.1

- replaced unknown package inventory with the confirmed empty initializer and absent proposed-module state;
- recorded the `0.0.0` greenfield package metadata without claiming build/install readiness;
- confirmed neighboring source-root/test READMEs and newspaper/LOC source-catalog coverage;
- recorded that expected dedicated tests, fixtures, and SourceDescriptor instances did not surface;
- converted illustrative module, live-flag, error, and test text into explicitly proposed activation contracts;
- added product separation for page/image, OCR, corrected transcription, article/clipping, event reporting, legal notices, obituaries, and extraction outputs;
- aligned role guidance to the canonical enum and surfaced draft `observation`/OCR-role drift instead of hardcoding it;
- strengthened admission metadata, finite outcome, secret safety, rights/privacy/sensitivity, fixture placement, activation, evidence, and rollback rules;
- preserved v0.1's intake-only, RAW/QUARANTINE-only, OCR-is-not-truth, candidate-extraction, no-public-shortcut, and fail-closed boundaries.

---

## Rollback

This is a documentation-only update. Restore the exact prior README from blob:

```text
b725cf66a235d03037829592b1a2be31a8d2b057
```

Rolling back this document does not implement, activate, or disable a connector and must not alter any package code, SourceDescriptor, rights/privacy/sensitivity decision, RAW capture, quarantine record, receipt, proof, correction, or release history.

---

## Related files

- [`connectors/newspapers/README.md`](../../README.md)
- [`connectors/newspapers/src/README.md`](../README.md)
- [`connectors/newspapers/tests/README.md`](../../tests/README.md)
- [`connectors/README.md`](../../../README.md)
- [`docs/sources/catalog/newspapers/README.md`](../../../../docs/sources/catalog/newspapers/README.md)
- [`docs/sources/catalog/newspapers/ocr-full-text.md`](../../../../docs/sources/catalog/newspapers/ocr-full-text.md)
- [`docs/sources/catalog/newspapers/event-reporting.md`](../../../../docs/sources/catalog/newspapers/event-reporting.md)
- [`docs/sources/catalog/newspapers/legal-notices.md`](../../../../docs/sources/catalog/newspapers/legal-notices.md)
- [`docs/sources/catalog/newspapers/obituaries.md`](../../../../docs/sources/catalog/newspapers/obituaries.md)
- [`docs/sources/catalog/loc/README.md`](../../../../docs/sources/catalog/loc/README.md)
- [`docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`docs/doctrine/directory-rules.md`](../../../../docs/doctrine/directory-rules.md)
- [`data/registry/sources/README.md`](../../../../data/registry/sources/README.md)
- [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../../../schemas/contracts/v1/source/source_descriptor.schema.json)
- [`fixtures/README.md`](../../../../fixtures/README.md)

---

KFM rule: `connectors/newspapers/src/newspapers/` is a bounded source-admission implementation package. It does not decide newspaper truth, transcription truth, identity, relationship, event, place, rights, privacy, sensitivity, proof, release, publication, public presentation, or generated-answer truth.

[Back to top](#top)
