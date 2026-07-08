<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-docs-terminology-parity-readme
title: tools/validators/docs/terminology-parity README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-docs-steward-plus-terminology-steward-plus-ci-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; docs-validator; terminology-parity; glossary-aware; non-authoritative
owning_root: tools/
responsibility: proposed documentation terminology-parity validator lane for canonical term casing, controlled vocabulary posture, deprecated synonym detection, glossary/authority-pointer alignment, source-role/truth-label consistency, and docs-QA reports without deciding doctrine, term meaning, evidence sufficiency, source admissibility, or release approval
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../_common/README.md
  - ../link-check/README.md
  - ../meta-block/README.md
  - ../stale-scan/README.md
  - ../../../docs/README.md
  - ../../../../docs/README.md
  - ../../../../docs/sources/catalog/GLOSSARY.md
  - ../../../../docs/doctrine/truth-posture.md
  - ../../../../docs/registers/DOCUMENT_REGISTRY.md
  - ../../../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../../../docs/adr/
  - ../../../../data/receipts/validation/
  - ../../../../artifacts/qa/
  - ../../../../tests/
notes:
  - "This README documents a proposed docs terminology-parity validator lane. It does not confirm executable files."
  - "A terminology-parity checker can report term casing drift, deprecated synonyms, glossary mismatch, source-role vocabulary drift, truth-label drift, and missing authority pointers. It cannot decide term meaning, doctrine acceptance, evidence sufficiency, source admissibility, policy exceptions, or release approval."
  - "KFM glossary material is a navigation aid unless the owning authority pointer says otherwise; validators must report drift without converting convenience glossaries into doctrine."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/docs/terminology-parity

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-docs--terminology--parity-informational)
![authority](https://img.shields.io/badge/authority-QA--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/docs/terminology-parity/` is the proposed documentation terminology-parity validator lane for Markdown files: canonical KFM term casing, controlled vocabulary posture, deprecated synonyms, source-role labels, truth-label labels, authority-pointer alignment, glossary drift, and docs-QA reports.

---

## Purpose

`tools/validators/docs/terminology-parity/` exists for terminology consistency checks over repository documentation and README-style Markdown.

The durable KFM question for this lane is:

> Does a document use KFM terms consistently with the accepted glossary, doctrine, contracts, schemas, and authority pointers, without treating the terminology scan as the authority for term meaning?

The answer should be a deterministic validation result and, where configured, a docs QA report. It should not edit doctrine, decide canonical terminology by itself, approve ADRs, validate evidence sufficiency, decide source admissibility, promote releases, or publish documents.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/docs/terminology-parity/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Terminology-parity validator executables | **PROPOSED / NEEDS VERIFICATION** | No script name is claimed here. |
| Source catalog glossary | **CONFIRMED in repo evidence / draft** | `docs/sources/catalog/GLOSSARY.md` exists and states it is a convenience register, not term authority by itself. |
| Parent docs-tooling boundary | **CONFIRMED in repo evidence / draft** | `tools/docs/README.md` says docs tooling can detect documentation drift but cannot decide truth, admissibility, or release approval. |
| Related docs validator lanes | **CONFIRMED README siblings / executable proposed** | `link-check/`, `meta-block/`, and `stale-scan/` README lanes exist; executable behavior remains unverified. |
| Canonical vocabulary profile | **PROPOSED / NEEDS VERIFICATION** | Accepted term list, casing rules, synonym map, and deprecation map must be approved outside this README before CI enforcement. |
| CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not prove CI, pre-commit, scheduled checks, or artifact uploads are wired. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Docs terminology-parity validator entrypoints | `tools/validators/docs/terminology-parity/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Link-check validator lane | `tools/validators/docs/link-check/` |
| Meta-block validator lane | `tools/validators/docs/meta-block/` |
| Stale-scan validator lane | `tools/validators/docs/stale-scan/` |
| General docs tooling | `tools/docs/` |
| Documentation content | `docs/` and each owning responsibility root |
| Glossaries and navigation registers | `docs/` lanes, with authority pointers inside each glossary/register |
| Authoritative term meaning | accepted doctrine, encyclopedia, contracts, schemas, standards, and ADRs |
| Policy rules | `policy/` |
| Receipts from validation runs | `data/receipts/validation/` or accepted receipt home |
| QA artifacts and summaries | `artifacts/qa/` when non-authoritative and non-trust-bearing |
| Tests and fixtures | `tests/` and accepted fixture conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** terminology-parity validator code may live here when it checks term usage, casing, synonym, and authority-pointer consistency.
- **NEEDS VERIFICATION:** exact executable names, vocabulary source, casing profile, deprecated-term list, fixture paths, report destinations, ignore rules, and CI wiring.
- **DENY:** using this folder as docs content authority, doctrine authority, glossary authority, ADR authority, term-meaning authority, source-admissibility authority, policy authority, evidence validator, release validator, receipt store, generated-docs store, or public documentation surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/docs/terminology-parity/` include checks that:

- detect inconsistent casing for KFM terms such as `EvidenceBundle`, `EvidenceRef`, `ReleaseManifest`, `RollbackCard`, `PolicyDecision`, `ReviewRecord`, `SourceDescriptor`, `spec_hash`, and `KFM_META_BLOCK_V2`;
- detect flattening of KFM-specific compound terms into generic wording where doctrine requires the exact form;
- detect deprecated synonyms or legacy names after an ADR or glossary update;
- detect mismatched truth labels, such as using `CONFIRMED` where the surrounding evidence only supports `PROPOSED`, `NEEDS VERIFICATION`, or `UNKNOWN`;
- detect source-role vocabulary drift where configured source-role terms are collapsed, renamed, or invented;
- check that convenience glossary entries include authority pointers instead of acting as authority themselves;
- check that docs use compatible terminology for artifact families such as receipts, proofs, catalog records, release manifests, and published artifacts;
- delegate broken authority links to `link-check/`;
- delegate stale glossary or review dates to `stale-scan/`;
- delegate malformed metadata fields to `meta-block/`;
- emit deterministic docs QA summaries and validation receipts where configured.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/docs/terminology-parity/` | Correct home |
|---|---|
| Documentation content | `docs/` or the owning root |
| Doctrine decisions | accepted doctrine / ADR lanes under `docs/` |
| Glossary authority decisions | accepted glossary, encyclopedia, contract, schema, standard, or ADR lanes |
| Policy rules | `policy/` |
| Contracts or schemas | `contracts/`, `schemas/` |
| EvidenceBundle validation | evidence/proof validator lanes |
| Receipts | `data/receipts/` |
| Proofs | `data/proofs/` |
| Release decisions or release manifests | `release/` |
| Published docs or public site output | accepted public/docs publishing root |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |

[Back to top](#top)

---

## Terminology-parity posture

Terminology parity is documentation QA, not governance approval.

A passing terminology-parity check means only that the configured validator did not detect configured term drift at scan time. It does not mean:

- the document is authoritative;
- the terms are fully and finally defined;
- the claims in the document are true;
- the glossary is the authority for a load-bearing decision;
- the source is admissible;
- the policy posture is correct;
- the implementation maturity is proven;
- the release state is approved;
- the document is safe for public publication.

A failing terminology-parity check should route to one of these actions:

- correct the term casing or spelling;
- add an authority pointer;
- update a glossary or terminology register through the owning docs lane;
- open a docs verification backlog item;
- propose an ADR for unresolved terminology conflict;
- add a documented ignore rule with owner, reason, scope, and review posture.

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `DOC_TERMINOLOGY_PARITY_PASS` | Configured terminology-parity checks passed. |
| `DOC_TERMINOLOGY_PARITY_FAIL` | One or more configured terminology-parity checks failed. |
| `TERM_CASING_MISMATCH` | Term appears with casing outside the accepted profile. |
| `DEPRECATED_TERM_USED` | Deprecated synonym or legacy name appears. |
| `CANONICAL_TERM_MISSING` | Expected canonical term is absent where the profile requires it. |
| `AUTHORITY_POINTER_MISSING` | Convenience glossary/register term lacks authority pointer. |
| `AUTHORITY_POINTER_CONFLICT` | Term points to conflicting authorities. |
| `TRUTH_LABEL_MISMATCH` | Truth label use appears inconsistent with surrounding evidence posture. |
| `SOURCE_ROLE_VOCAB_DRIFT` | Source-role vocabulary is collapsed, renamed, invented, or missing. |
| `ARTIFACT_FAMILY_COLLAPSE` | Receipt/proof/catalog/publication terminology is conflated. |
| `DELEGATE_TO_LINK_CHECK` | Authority-link resolution should be checked by the link-check lane. |
| `DELEGATE_TO_META_BLOCK` | Metadata term issue should be checked by the meta-block lane. |
| `DELEGATE_TO_STALE_SCAN` | Staleness or review-age issue should be checked by the stale-scan lane. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/docs/terminology-parity/
├── README.md
├── test_docs_terminology_parity.py
└── fixtures/
    ├── valid_canonical_terms/
    ├── term_casing_mismatch/
    ├── deprecated_term_used/
    ├── missing_authority_pointer/
    ├── conflicting_authority_pointer/
    ├── truth_label_mismatch/
    ├── source_role_vocab_drift/
    ├── artifact_family_collapse/
    └── ignored_with_reason/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/docs/terminology-parity
```

```bash
python tools/validators/docs/terminology-parity/check_terminology_parity.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `check_terminology_parity.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator uses an accepted vocabulary profile rather than hidden tool-only doctrine.
- [ ] Validator reports terminology drift without deciding term meaning by itself.
- [ ] Convenience glossary entries remain navigation aids unless an authority pointer says otherwise.
- [ ] Truth-label and source-role checks preserve KFM evidence posture.
- [ ] Receipt/proof/catalog/publication family terms remain distinct.
- [ ] Link resolution is delegated to link-check tooling where appropriate.
- [ ] Metadata parse/field checks are delegated to meta-block tooling where appropriate.
- [ ] Stale review and glossary age checks are delegated to stale-scan tooling where appropriate.
- [ ] Ignore rules include reason, owner, scope, and review posture.
- [ ] Reports and receipts are written only to accepted non-authority roots.
- [ ] Validator does not edit docs without a separate explicit change process.
- [ ] Tests use synthetic fixtures and do not require network access by default.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty file. |
| Next smallest safe change | Verify actual terminology-parity scripts, accepted vocabulary profile, deprecated-term map, ignore files, fixtures, report destinations, receipts, and CI wiring before promoting this lane beyond draft. |
