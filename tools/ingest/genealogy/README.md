<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-ingest-genealogy-readme
title: tools/ingest/genealogy README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-people-dna-land-steward-plus-sensitivity-reviewer
created: 2026-07-07
updated: 2026-07-07
policy_label: restricted; deny-by-default; no-living-person-public-output; no-raw-dna
owning_root: tools/
responsibility: proposed genealogy ingest helper boundary for evidence-bound, privacy-aware, review-only source normalization
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../../README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/domains/people-dna-land/ARCHITECTURE.md
  - ../../../docs/domains/people-dna-land/sublanes/genealogy.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../docs/domains/people-dna-land/CONSENT.md
  - ../../../docs/domains/people-dna-land/CONSENT_MODEL.md
  - ../../../docs/domains/people-dna-land/CONSENT_REGISTER.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../contracts/domains/people-dna-land/genealogy/README.md
  - ../../../data/registry/sources/
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../data/proofs/
  - ../../../policy/
  - ../../../release/
notes:
  - "This README defines a proposed genealogy ingest tooling boundary, not a confirmed implementation."
  - "Genealogy imports are assertion-first and evidence-bound. GEDCOM, tree overlays, vital-record extracts, cemetery/obituary/census/court/probate records, and similar material enter as source evidence or candidate assertions, not canonical person truth."
  - "Living-person output, DNA-derived relationships, raw kit/vendor identifiers, raw DNA segments, and private person-parcel joins are deny-by-default and must not be published by this lane."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/ingest/genealogy

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-genealogy--ingest--helpers-informational)
![sensitivity](https://img.shields.io/badge/sensitivity-deny--by--default-red)
![publication](https://img.shields.io/badge/publication-never--from--ingest-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/ingest/genealogy/` is the proposed tooling lane for conservative genealogy source-admission helpers: parse, normalize, fingerprint, redact, and report genealogical source material for steward review without creating public person truth, living-person output, DNA inference, land-title claims, or publication artifacts.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Placement and authority note](#placement-and-authority-note)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Genealogy ingest posture](#genealogy-ingest-posture)
- [Sensitivity and consent posture](#sensitivity-and-consent-posture)
- [Inputs and outputs](#inputs-and-outputs)
- [Report envelope](#report-envelope)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/ingest/genealogy/` exists to hold durable, repo-wide helper logic for **genealogy source intake support** under the People / Genealogy / DNA / Land Ownership governance model.

This lane may help parse or inspect GEDCOM-like files, family-tree exports, public vital-record extracts, cemetery records, obituary snippets, church/school/military/census/directory/court/probate records, and other genealogy-adjacent evidence packages. It may produce normalized candidate rows, fingerprints, source-shape reports, redaction-preview reports, or quarantine reasons.

The durable KFM question for this lane is:

> Can this genealogy source material be represented as reviewable, evidence-bound candidate assertions without weakening privacy, consent, DNA, cultural, land-title, or publication controls?

The answer should be a governed intake report or candidate handoff. It should never be a public person profile, confirmed family relationship, canonical identity, DNA-derived relationship, land-title claim, or publication decision.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/ingest/genealogy/README.md` | **CONFIRMED** | This README replaces the short scaffold with a governed tooling-lane boundary. |
| Genealogy ingest executable | **PROPOSED-to-create** | No script name is claimed as implemented by this README. |
| Parent `tools/ingest/README.md` | **NEEDS VERIFICATION / absent in recent checks** | Parent lane README should be added before expanding ingest tooling broadly. |
| People / Genealogy / DNA / Land architecture | **CONFIRMED in repo evidence** | Domain architecture exists and sets deny-by-default living-person and DNA controls. |
| Genealogy sublane docs | **CONFIRMED in repo evidence / sublane split CONFLICTED** | Genealogy sublane exists but notes unresolved three-way vs four-way sublane split. |
| Sensitivity profile | **CONFIRMED in repo evidence** | Sensitivity profile sets strong deny-by-default posture for living-person, DNA, and private person-parcel surfaces. |
| Source registry / descriptors | **NEEDS VERIFICATION** | SourceDescriptor activation and source-specific rights must be checked before relying on any source. |
| Publication authority | **DENY here** | Ingest helpers do not publish. |
| Canonical person identity | **DENY here** | Ingest helpers do not create `PersonCanonical` truth. |
| Living-person public output | **DENY here** | No public output from this lane may expose living-person fields. |
| Raw DNA / DNA-derived relationship output | **DENY here** | Raw DNA and DNA-derived relationships require separate restricted governance and must not be emitted here. |

> [!IMPORTANT]
> This folder is a tooling boundary, not a source of person truth. Every imported person, name, event, residence, relationship, and family grouping remains an assertion or candidate until reviewed through the owning contracts, schemas, policies, EvidenceBundle path, and release controls.

[Back to top](#top)

---

## Placement and authority note

`tools/` is the repo-wide tooling root for durable executable support. `docs/domains/people-dna-land/` owns human-facing domain doctrine. `contracts/` owns object meaning. `schemas/` owns field-level shape. `policy/` owns admissibility and release rules. `data/registry/sources/` owns source activation and source-role truth. `data/raw/` and `data/quarantine/` own source-material lifecycle entry points. `release/` owns release decisions.

Safe interpretation for this path:

- **CONFIRMED:** this README exists at `tools/ingest/genealogy/README.md`.
- **PROPOSED:** genealogy ingest helper code may live here if it is deterministic, bounded, rights-aware, consent-aware, and unable to publish.
- **NEEDS VERIFICATION:** whether `tools/ingest/` should become a broader canonical sub-tree under `tools/`.
- **NEEDS VERIFICATION:** whether standalone genealogy tooling should remain separate or fold into broader People / DNA / Land tooling after the sublane ADR is resolved.
- **DENY:** any use of this path as a canonical person store, family-tree publication surface, DNA interpretation surface, land-title authority, living-person release path, or policy authority.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A genealogy ingest helper may parse, fingerprint, normalize, redact-preview, or report on source material. It does not move information across lifecycle phases by itself.

Required boundary rules:

1. **Ingest output is not publication.** It can create a candidate handoff or review report, not a public person or family page.
2. **GEDCOM and tree imports remain RAW.** They must not be public, mapped directly, or used as canonical identifiers.
3. **Every person claim remains an assertion.** Imported records do not become `PersonCanonical` objects without review.
4. **Every relationship remains an assertion or hypothesis.** A parent/child/spouse edge is not confirmed solely because a source file says so.
5. **Living-person fields fail closed.** Unknown living status should be treated conservatively until policy and review permit a safer disposition.
6. **DNA-derived content is outside this lane.** DNA match evidence, segments, kit tokens, and DNA-derived relationship hypotheses require restricted DNA governance.
7. **Person-parcel joins are outside this lane.** Private person-land joins are denied by default and require separate land/title governance.
8. **Receipts and proofs are separate.** Ingest reports may point to receipt/proof workflows, but this folder does not own trust artifacts.
9. **AI and UI remain downstream.** No Focus Mode, map, drawer, dashboard, or AI response may read from this ingest lane or treat its output as public truth.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/ingest/genealogy/` include:

- GEDCOM / GEDZip shape checkers.
- Tree-export metadata fingerprint helpers.
- Candidate `PersonAssertion` extraction helpers.
- Candidate `NameAssertion` extraction helpers.
- Candidate `LifeEvent`, `ResidenceEvent`, or `MigrationEvent` extraction helpers.
- Candidate relationship-edge extraction helpers that label all edges as assertions or hypotheses.
- Source-role and rights preflight checks.
- Living-status heuristic flaggers that produce review flags, not public decisions.
- Consent-reference preflight checks that verify a consent pointer exists without deciding release.
- Redaction-preview helpers for living-person fields and private notes.
- Quarantine-reason emitters.
- Ingest run report generators.
- Dry-run CLI wrappers for local review.
- No-network fixture adapters for tests.

A helper belongs here only when it is:

- deterministic;
- network-free by default;
- explicit about source descriptor references;
- explicit about source role and rights posture;
- conservative about living-person uncertainty;
- unable to publish or create canonical person truth;
- unable to emit raw DNA, raw kit identifiers, or DNA segment data;
- tested with synthetic or public-safe fixtures;
- explicit about its output envelope and finite outcomes.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/ingest/genealogy/` | Correct home | Reason |
|---|---|---|
| Genealogy domain doctrine | `docs/domains/people-dna-land/` | Human-facing doctrine is not executable tooling. |
| Object contracts | `contracts/domains/people-dna-land/` | Object meaning belongs in contracts. |
| JSON Schemas | `schemas/contracts/v1/...` | Field shape belongs in schemas. |
| Policy rules | `policy/` | Ingest code does not own admissibility or release policy. |
| Source descriptors | `data/registry/sources/` | Source activation, rights, role, and cadence belong in source descriptors. |
| Raw uploaded genealogy files | `data/raw/...` or `data/quarantine/...` | Data lifecycle roots own source material. |
| Processed person assertions | `data/processed/...` | Transformation outputs are not tool code. |
| Catalog or triplet records | `data/catalog/`, `data/triplets/` | Catalog and graph projection have their own roots. |
| Receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts are stored outside tooling. |
| Release manifests or rollback cards | `release/` | Release authority is separate. |
| Canonical person store | governed domain data store, if accepted | Ingest helpers do not resolve identity. |
| DNA match interpretation | DNA sublane and restricted policy surfaces | DNA evidence is deny-by-default and outside genealogy ingest helpers. |
| Public family trees or profile pages | released, governed public products only after policy gates | Public output cannot come from ingest. |
| Tests | `tests/ingest/genealogy/` or existing test convention | Tests prove this lane; they are not the lane itself. |
| Fixtures containing real living persons | nowhere public | Fixtures must be synthetic, public-domain-safe, or fully redacted. |

[Back to top](#top)

---

## Genealogy ingest posture

The genealogy ingest helper should be understood as an **evidence intake assistant**.

It may create:

- a source-shape report;
- a candidate assertion report;
- a rights and source-role preflight report;
- a living-status review flag report;
- a redaction-preview report;
- a quarantine-reason report;
- a proposed work record;
- a reviewer handoff file.

It must not create:

- a public profile;
- a public family tree;
- a canonical person identity;
- a confirmed genealogy relationship;
- a DNA-derived relationship claim;
- a land ownership or title claim;
- an EvidenceBundle;
- a policy decision;
- a release manifest;
- a public map layer;
- an AI answer.

If a future helper emits a `PROPOSED_WORK_RECORD`, that record should state what was parsed, what was withheld, what needs review, what source and consent references were available, and what downstream validation must happen next. It should not say the claim is true or approved.

[Back to top](#top)

---

## Sensitivity and consent posture

Genealogy is one of the strongest default-deny surfaces in KFM.

Minimum handling rules:

| Concern | Required posture |
|---|---|
| Living-person fields | Fail closed. Unknown living status should be held or redacted until reviewed. |
| Names and aliases | Treat as `NameAssertion`, not canonical identity. |
| Birth, marriage, death, residence, migration | Treat as evidence-bound `LifeEvent`, `ResidenceEvent`, or `MigrationEvent` candidates. |
| Parent / child / spouse / sibling links | Treat as `RelationshipAssertion` or `RelationshipHypothesis` until reviewed. |
| Tree owner notes and private notes | Quarantine or redact by default. |
| GEDCOM IDs and vendor/tree IDs | Internal only; never public identifiers. |
| DNA kit/vendor identifiers | Denied here; do not parse or emit from this lane. |
| DNA segment data | Denied here; restricted DNA governance only. |
| Person-parcel joins | Denied here; separate land/title governance required. |
| Cultural, burial, tribal, adoption, guardianship, or sensitive family contexts | Prefer quarantine, redaction, restricted review, or denial. |
| Consent and revocation | Reference only through governed consent surfaces; revocation must be enforced downstream. |

The safe default is `ABSTAIN`, `QUARANTINE`, or `DENY_PUBLIC_OUTPUT` when rights, living status, consent, source role, or sensitivity cannot be resolved.

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- Source descriptor references.
- GEDCOM / GEDZip fixtures or uploaded files routed through lifecycle controls.
- Family-tree export metadata.
- Public vital-record extracts.
- Cemetery, obituary, church, school, military, census, directory, court, and probate source extracts.
- Consent-reference metadata.
- Public-safe synthetic fixtures.
- Redaction policy references.

### Unsuitable inputs

- raw DNA data;
- raw DNA segment files;
- raw kit or vendor identifiers;
- private living-person records outside a governed source and consent boundary;
- private notes from family-tree systems without explicit rights review;
- adoption, guardianship, tribal, cultural, or burial-sensitive details without steward review;
- person-parcel joins;
- credentials or API tokens;
- source material that bypasses `data/raw/` or `data/quarantine/` lifecycle handling.

### Suitable outputs

- ingest JSON report;
- source-shape report;
- candidate assertion report;
- redaction-preview report;
- quarantine-reason report;
- proposed work record candidate;
- reviewer handoff summary.

Outputs should be written only to explicit caller-selected paths. A helper should not silently write into `data/receipts/`, `data/proofs/`, `data/catalog/`, `data/triplets/`, `data/published/`, or `release/`.

[Back to top](#top)

---

## Report envelope

A first-slice genealogy ingest report should be compact, deterministic, and privacy-preserving.

```json
{
  "tool": "genealogy-ingest",
  "status": "QUARANTINE_REVIEW_REQUIRED",
  "source_id": "genealogy_source_placeholder",
  "input_kind": "gedcom",
  "source_role": "candidate",
  "counts": {
    "person_assertion_candidates": 12,
    "relationship_assertion_candidates": 9,
    "life_event_candidates": 18,
    "living_status_unknown": 4,
    "withheld_private_notes": 3
  },
  "sensitivity": {
    "living_person_public_output": false,
    "raw_dna_present": false,
    "dna_derived_relationships_present": false,
    "person_parcel_join_present": false,
    "public_release_candidate": false
  },
  "decision": {
    "outcome": "QUARANTINE_REVIEW_REQUIRED",
    "reason_codes": ["LIVING_STATUS_UNKNOWN", "SOURCE_RIGHTS_NEED_REVIEW"],
    "blocking": true
  },
  "next_review": [
    "confirm source descriptor",
    "confirm rights and consent posture",
    "review living-status flags",
    "route candidate assertions through contracts and schemas",
    "do not publish without EvidenceBundle, PolicyDecision, ReviewRecord, ReleaseManifest, and rollback path"
  ]
}
```

The report may be used by reviewers or CI. It is not a receipt unless a separate receipt workflow adopts and stores it under the proper lifecycle root.

[Back to top](#top)

---

## Validation

Recommended first test surface:

```text
tests/ingest/genealogy/
├── README.md
├── test_genealogy_ingest.py
└── fixtures/
    ├── public_domain_family_tree/
    │   ├── input.ged
    │   └── expected_report.json
    ├── living_status_unknown/
    │   ├── input.ged
    │   └── expected_report.json
    ├── private_notes_present/
    │   ├── input.ged
    │   └── expected_report.json
    ├── dna_fields_present/
    │   ├── input.json
    │   └── expected_report.json
    └── malformed_input/
        ├── input.ged
        └── expected_report.json
```

Recommended assertions:

- public-safe synthetic input returns candidate assertion counts without public output;
- living-status unknown records return `QUARANTINE_REVIEW_REQUIRED` or `DENY_PUBLIC_OUTPUT`;
- private notes are withheld or quarantined, not copied into public reports;
- DNA-like fields return `DENY_UNSUPPORTED_INPUT` or a restricted-lane handoff, not parsed relationship output;
- GEDCOM identifiers are not emitted as public IDs;
- relationship edges are labelled as assertions or hypotheses;
- missing source descriptor reference blocks promotion-oriented outputs;
- generated reports are deterministic;
- no test fixture contains real living-person private data;
- no helper writes to lifecycle or release roots without explicit workflow control.

Suggested future command pattern:

```bash
pytest -q tests/ingest/genealogy
```

```bash
python tools/ingest/genealogy/genealogy_ingest.py \
  --input tests/ingest/genealogy/fixtures/public_domain_family_tree/input.ged \
  --source-id genealogy_source_placeholder \
  --output .tmp/genealogy-ingest-report.json \
  --dry-run
```

> [!NOTE]
> The command above is a proposed interface, not proof that `genealogy_ingest.py` exists.

[Back to top](#top)

---

## Review checklist

Before adding or changing genealogy ingest code, reviewers should confirm:

- [ ] The helper is ingest/report-only and cannot publish.
- [ ] All person records remain assertions or candidates.
- [ ] Relationship edges remain assertions or hypotheses until reviewed.
- [ ] Living-person fields fail closed.
- [ ] GEDCOM or tree IDs are not public identifiers.
- [ ] Private notes are withheld or quarantined by default.
- [ ] DNA fields, raw kits, vendor IDs, and segment data are denied or routed to restricted DNA governance.
- [ ] Person-parcel joins are denied here.
- [ ] Source descriptor fields are referenced, not duplicated as authority.
- [ ] Rights and consent posture are surfaced as review requirements.
- [ ] Network access is off by default.
- [ ] Outputs are deterministic and machine-readable.
- [ ] Tests use synthetic or public-safe fixtures only.
- [ ] The helper does not write directly to `data/catalog/`, `data/triplets/`, `data/published/`, `data/proofs/`, `data/receipts/`, or `release/`.
- [ ] Any proposed work record points to downstream validation, review, correction, and rollback requirements.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace short scaffold with governed ingest-lane contract | **DONE in this README** | Establishes genealogy ingest boundaries and default-deny posture. |
| Add parent `tools/ingest/README.md` | **PROPOSED** | Clarifies broader ingest tooling under `tools/`. |
| Resolve genealogy sublane split | **NEEDS VERIFICATION / ADR-class** | Prevents accidental authority split between `people` and `genealogy`. |
| Add `genealogy_ingest.py` dry-run helper | **PROPOSED** | Emits deterministic report from synthetic/public-safe input. |
| Add public-safe fixtures | **PROPOSED** | Proves candidate extraction, living-status quarantine, private-note withholding, DNA denial, and malformed-input behavior. |
| Align report envelope with contracts/schemas | **PROPOSED / NEEDS VERIFICATION** | Match accepted People / Genealogy / DNA / Land contracts when available. |
| Wire into CI as non-blocking review signal | **PROPOSED / later** | Surfaces source-shape and sensitivity issues without publication side effects. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing scaffold. |
| Next smallest safe change | Add parent `tools/ingest/README.md`, then add `tools/ingest/genealogy/genealogy_ingest.py` with synthetic fixtures under `tests/ingest/genealogy/`. |
